import requests
from bs4 import BeautifulSoup


def query(query):
    url = 'https://www.google.com/search?q={0}&tbm=isch'.format(query)
    content = requests.get(url).content
    soup = BeautifulSoup(content,'lxml')
    images = soup.findAll('img')
    return images[1].get('src')
      