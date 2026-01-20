from urllib import request
from bs4 import BeautifulSoup

"""This program scrapes data from a webpage using urllib.request and
BeautifulSoup libraries. 
It looks for the hrefs content inside a webpage that is in position A and print them with 
an index. Then it follows the link in position A and repeats the process a selected number of times.

It accepts as input the webpage URL and uses the tag 'a' as search pattern(though it has the ability to accept tag input).
The other inputs are the position of the link to follow and the number of times to repeat the process."""

# instructions to input
url = input('Enter URL - ') # enter URL
find = 'a' #input('Enter tag - ') # enter tag to search for
position = input('Enter position - ') # position of link selected
times = input('Repeating times - ') # amount of times repeating the cycle

html = request.urlopen(url).read() # open URL using urllib.request
soup = BeautifulSoup(html, 'html.parser') # parse the content of the page into an object

# retrieve selected anchor tags
tags = soup(find)
n = 1
recur_url = None
while n <= int(times):
    print(f'Round {n}')
    indx = 1
    if recur_url:
        html = request.urlopen(recur_url).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup(find)
        for indx,tag in enumerate(tags, 1):
            page_url = tag.get('href', None)
            if indx == int(position):
                current_url = page_url
                print(f'URL {indx}: {current_url}')
            indx = indx + 1
    else:
        for indx,tag in enumerate(tags, 1):
            page_url = tag.get('href', None)
            if indx == int(position):
                current_url = page_url
                print(f'URL {indx}: {current_url}')
            indx = indx + 1
    recur_url = current_url
    n = n + 1
