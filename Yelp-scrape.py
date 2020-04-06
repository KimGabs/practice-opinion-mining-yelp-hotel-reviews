"""
done in 

Yelp

"""
# Gathering The Data
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# # Analysing The Data
import pandas as pd
import numpy as np


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get(url, headers=headers)

    if not response.ok:
        print('server responded: ', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
        print('server responded: ', response.status_code)

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
        num_reviews = int(num_reviews.text.strip().split(' ')[0])
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

    print(num_reviews)
    return(num_reviews)


def every_page(num_reviews):
    url_list = []
    for i in range(0, num_reviews, 20):
        url_list.append(
            'https://www.yelp.com/biz/manila-marriott-hotel-manila-2?osq=Hotels=' + str(i))
    return(url_list)


def main():
    url = 'https://www.yelp.com/biz/manila-marriott-hotel-manila-2?osq=Hotels'
    get_page(url)
    # num_reviews = get_detail_data(get_page(url))
    # url_list = every_page(num_reviews)
    # print(num_reviews)
    # for i in range(len(url_list)):
    #     num_reviews = get_detail_data(get_page(url_list[i]))
    #     print(num_reviews)


if __name__ == '__main__':
    main()
