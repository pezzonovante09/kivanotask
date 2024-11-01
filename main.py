from bs4 import BeautifulSoup as BS
import requests
import csv

def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='list-view')
    phones = catalog.find_all('div', class_='item product_listbox oh')
    for phone in phones:
        try:
            title = phone.find('div', class_='listbox_title oh').text
        except:
            title = ''
        try:
            price = phone.find('div', class_='listbox_price text-center').text
        except:
            price =''
        try:
            image = phone.find('img').get('src')
            image = f'https://kivano.kg{image}'
        except:
            image = ''
        data = {
            'title': title,
            'price': price,
            'image': image
        }

        write_csv(data)

def write_csv(data):
    with open('phones.csv', 'a') as csv_files:
        names = ['title', 'price', 'image']
        writer = csv.DictWriter(csv_files, delimiter='|', fieldnames=names)
        writer.writerow(data)

def main():
    url = 'https://www.kivano.kg/mobilnye-telefony'
    html = get_html(url)
    data = get_data(html)
main()