"""
done in 

Yelp

"""

import requests
from bs4 import BeautifulSoup


def get_page(url):
    response = requests.get(url)

    if not response.ok:
        print('server responded: ', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_detail_data(soup):
    # user_review

    # hotel_name
    try:
        name = soup.find('h1', attrs={'class': 'lemon--h1__373c0__2ZHSL'}).text
    except:
        name = ''

    # rating
    try:
        rating = soup.find('div', role='img').get('aria-label')
        rating = rating.strip().split(' ')[1]
    except:
        rating = ''

    # number_of_reviews
    try:
        num_reviews = soup.find('p', attrs={
            'class': 'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--mid__373c0__3G312 text-align--left__373c0__2pnx_ text-size--large__373c0__1568g'})
        num_reviews = num_reviews.text.strip().split(' ')[0]
    except:
        num_reviews = ''

    print(rating)


def main():
    url = 'https://www.yelp.com/biz/manila-marriott-hotel-manila-2?osq=Hotels'
    get_detail_data(get_page(url))


if __name__ == '__main__':
    main()
