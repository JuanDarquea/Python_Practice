from bs4 import BeautifulSoup
from urllib import request
#from lxml import etree # lxml is another library that can be used for HTML parsing 

url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

with request.urlopen(url) as response:
    data = response.read()
    print(f'Retrieving {url}')
    print(f'\nRetrieved',len(data),'characters')
    
    soup = BeautifulSoup(data, 'xml')
    comments = soup.find_all('count')
#    for i, comment in enumerate(comments, 1):
#        print(f"Comment {i}:", comment.text)

    counts = [int(comment.text) for comment in comments]    
    print('Total comments:', len(counts))
    print('Sum of comments:', sum(counts))
#    print(data.decode())