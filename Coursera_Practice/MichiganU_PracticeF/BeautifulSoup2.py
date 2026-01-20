from urllib import request
from bs4 import BeautifulSoup

"""This program scrapes data from a page using urllib.request and 
BeautifulSoup. It is set to look for a number in said
content, count and sum those numbers.
Giving as output the total count of numbers and the sum of them all.

It accepts as input the page URL (first input) and 
the tag as search pattern (second input)."""

url = input('Enter URL - ') # enter URL
html = request.urlopen(url).read() # open URL using urllib.request
soup = BeautifulSoup(html, 'html.parser') # parse the content of the page into an object

# retrieve all of the anchor tags
find = input('Enter tag - ')
tags = soup(find)
sum = 0
content_list = []
for count,tag in enumerate(tags, 0):
    page_url = tag.get('class', None)
    content = int(tag.contents[0])
    content_list.append(content)
    sum = sum + content
    count = count + 1
print()
print(f'Count {count}', f'\nSum {sum}')
print()
print(content_list)
