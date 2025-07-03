# go to git bash
# git config --global user.name 'Subin Khatiwada'
# git config --global user.email 'Subinkhatiwada@gmail.com'

# git init
# git status => if you want to check what are the status of files
# git diff => if you want to check what are the changes
# git add .
# git commit -m 'your message'
# copy paste git code from github

import requests

from bs4 import BeautifulSoup

import json
import csv

url = 'http://books.toscrape.com/'

def get_books_data (url):
    response = requests.get(url)
    if response.status_code != 200:
        print('Page loading failed.')
        return
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    book_list = []

    for book in books:
        title = book.h3.a['title']
        price_text = book.find('p', class_='price_color').text
        currency = price_text[0]
        price = float(price_text[1:])
        print(title,currency,price)
        book_list.append(
            {
                'title': title,
                'currency': currency,
                'price': price,
            }
        )
    return (book_list)
    

all_books_list = get_books_data(url)
if all_books_list:
    with open('books.json', 'w', encoding='utf-8') as f:
        # use utf-8 encoding to handle spefial characters like $/£
        # without indent the json list comes in one long single line and asci false handles non ASCII characters.
        json.dump(all_books_list, f, indent=4, ensure_ascii=False) 
else:
    print('No book data was retrived.')


with open('AI_python/scrapper/books.csv', 'w', newline='', encoding='utf-8') as f:
    # writer = csv.DictReader(f, fieldnames=['title', 'currency', 'price']) # preferred way
    writer = csv.DictWriter(f, fieldnames=all_books_list[0].keys())
    writer.writeheader()
    writer.writerows(all_books_list)