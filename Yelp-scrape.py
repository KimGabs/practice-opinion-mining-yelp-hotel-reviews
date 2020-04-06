"""
done in 

Yelp

"""
# Gathering The Data
import requests
from bs4 import BeautifulSoup

# # Analysing The Data
# import pandas as pd
# import numpy as np


def get_page(url):
    response = requests.get(url)

    if not response.ok:
        print('server responded: ', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_detail_data(soup):

    # Name of the hotel
    try:
        name = soup.find('h1', attrs={'class': 'lemon--h1__373c0__2ZHSL'}).text
    except:
        name = ''

    # Hotel rating
    try:
        rating = soup.find('div', role='img').get('aria-label')
        rating = rating.strip().split(' ')[0]
    except:
        rating = ''

    # number of user reviews
    try:
        num_reviews = soup.find('p', attrs={
            'class': 'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--mid__373c0__3G312 text-align--left__373c0__2pnx_ text-size--large__373c0__1568g'})
        num_reviews = num_reviews.text.strip().split(' ')[0]
    except:
        num_reviews = ''
    # user review content
    try:
        usr_review = soup.find('span', lang='en').text
    except:
        usr_review = ''

    try:
        divs = soup.findAll('span', lang='en')
    except:
        divs = ''

    reviews = []
    for div in divs:
        reviews.append(div.text)

    print(reviews[18])


def main():
    url = 'https://www.yelp.com/biz/manila-marriott-hotel-manila-2?osq=Hotels'
    get_detail_data(get_page(url))


if __name__ == '__main__':
    main()
