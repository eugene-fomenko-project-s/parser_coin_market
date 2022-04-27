import csv

import requests
from bs4 import BeautifulSoup


def write_csv(data, f_name='new_file.csv'):
    with open(f_name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([data['Name'], data['Market_cap'], data['Price']])
    return f_name


def search_info():
    count = 0
    while 1:
        name = input('\nВведите название криптовалюты, для выхода введите q:\n')
        if name == 'q':
            return
        for item in csv.reader(open('new.csv')):
            if item[0] == name:
                print("рыночная капитализация:", item[1])
                print("стоимость 1 ед. в долларах США:", item[2])
                break
            count += 1


def take():
    url = 'https://coinmarketcap.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    trs = soup.find('tbody').find_all('tr', limit=10)
    name = ''
    cap = ''
    price = ''
    for tr in trs:
        tds = tr.find_all('div', class_='sc-16r8icm-0 sc-1teo54s-1 dNOTPP',limit=1)
        tds1 = tr.find_all('p', class_='sc-1eb5slv-0 hykWbK',limit=1)
        tds2 = tr.find_all('div', class_='sc-131di3y-0 cLgOOr',limit=1)
        for x in tds:
            texts = x.find_all('p', class_='sc-1eb5slv-0 iworPT')
            for text in texts:
                name = text.get_text()
        for x2 in tds2:
            texts2 = x2.find_all('a', class_='cmc-link')
            for text2 in texts2:
                price = text2.get_text()
        for x1 in tds1:
            texts1 = x1.find_all('span', class_='sc-1ow4cwt-1 ieFnWP')
            for text1 in texts1:
                cap = text1.get_text()
        data = {
            'Name': name,
            'Market_cap': cap,
            'Price': price
        }
        write_csv(data, "new.csv")


if __name__ == "__main__":
    take()
    search_info()
