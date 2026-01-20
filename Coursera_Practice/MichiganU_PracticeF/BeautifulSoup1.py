from urllib import request
from bs4 import BeautifulSoup

"""This program scrapes data from a webpage using urllib.request and
BeautifulSoup libraries. 
It looks for all the hrefs content inside a webpage and print them with 
an index.

It accepts as input the webpage URL and uses the tag 'a' as search pattern."""

url = input('Enter URL - ') # enter URL
html = request.urlopen(url).read() # open URL using urllib.request
soup = BeautifulSoup(html, 'html.parser') # parse the content of the page into an object

# retrieve all of the anchor tags
find = input('Enter tag - ')
tags = soup(find)
for indx,tag in enumerate(tags, 1):
    page_url = tag.get('href', None)
    print(f'URL {indx}: {page_url}')
    indx = indx + 1

