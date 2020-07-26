# Activate Virtual Environment
# !/usr/bin/env python

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://www.bu.edu/back2bu/'

# Opening connection, grab page
uClient = uReq(url)

page_html = uClient.read()

# Close connection
uClient.close()

# import requests
# page = requests.get(url)

# soup = soup(page.content, 'html.parser')
# print(soup.prettify())

# find = soup.find_all('li')
# print(find)

# import pdb; pdb.set_trace()


# Printing Contents
# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each sub-links
topics = page_soup.findAll("div", {"class": "bulp-item-content bulp-promo-content"})

sub_topics = page_soup.findAll("div", {"class": "bulp-item-button bulp-promo-button bulp-promo-area1-button button-primary"})

for link in soup.findAll('a', attrs= (({"class": "bulp-item-content bulp-promo-content"}), {'href': topics.compile("^http://")})):
    print(link.get('href'))
print(len(topics))

# print(topics)
# print("\n \n")
# print(sub_topics)
# print("\n \n \n \n")