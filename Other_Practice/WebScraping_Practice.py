import bs4
from bs4 import BeautifulSoup
import urllib
import requests
import wikipediaapi
import re
import csv

url1 = 'https://scrapepark.org/'


def sunset_sunrise_API():
    """
    Practice on the use of APIs via: 
    - sunset & sunrise API
    """
    # create our variables with a latitude and longitude value
    uio_ec = ['-0.180653', '-78.467838']
    gye_ec = ['-2.19616', '-79.88621']

    # input the city to select which 'lat' ang 'lng' to use
    city = input('Please select a city betweer "guayaquil" or "quito" as your city to look for data: ').lower()
    
    # create a if statement to choose between the city input selection
    if city == 'guayaquil':
        lat = gye_ec[0]
        lng = gye_ec[1]
    elif city == 'quito':
        lat = uio_ec[0]
        lng = uio_ec[1]

    date = '2025-12-24' # christmas date
    api = 'https://api.sunrisesunset.io/json?' # assign API to a variable
    res_data_keys = [] # create a dict to store the key and values obtained
    i = 0

    try:
        # call the API with the 'lat', 'lng' and 'date' data provided and assign it, with error handling integrated
        if city is not None:
            try:
                req = requests.get(f'{api}lat={lat}&lng={lng}&date={date}')
            except Exception as e:
                print(f'Failure to get a response from API: {e}')
            
            data = req.json() # create a variable with the json output obtained from the API
            data_keys = list(data.values()) # create an iterable list with the 'data' json output 

            print('Data status: ', f'{data_keys[1]}') # print the status of the API calling

            # create a for loop tha iterates through the items (.items()) in the results dict of the data variable
            for key, value in data['results'].items():
                i += 1
                print(f'Data {i} - {key}:{value}')
                res_data_keys.append(f'Data {i} - {key}:{value}') # append key and value with index from data to a new variable to create a file
        else:
            raise NameError
    except NameError:
        print('Failure to select a city. Please select one next time.', f'\nGoodbye!')
    except Exception as e:
        print(f'Error calling the API: {e}')

    # this part is optional
    q1 = f'\nWrite "yes" if ou want to create a file with the resulting information from the SUNSET & SUNRISE API'
    q2 = ' or "no" if you do not want to create a file with that information: '
    question1 = q1 + q2
    file_writing = input(question1).lower()
    if file_writing == 'yes':
        try:
            with open('File1.txt', 'w') as f:
                for key in res_data_keys:
                    f.write(f'{key}\n')

            print(f'\nFile written successfully!')
        except Exception as e:
            print(f'Error creating file: {e}')
    else:
        print('\nGoodbye!!')
        return

def wikipedia_API():
    """
    Docstring for wikipedia_API
    """
    # create an instance for wikipediaapi and create an object with the parameter languaje
    language = 'en'
    wiki_wiki = wikipediaapi.Wikipedia(user_agent='your_user_agent', language=language)

    # use method .page to make a request with a key_word
    key_word = 'Python (programming language)'
    wiki_python = wiki_wiki.page(key_word)

    print('Title:', wiki_python.title.capitalize())
    print(f'Summary: ', f'\n{wiki_python.summary}')
    print(f'\nURL:', wiki_python.fullurl)

def call_soup():
    """
    
    """
    print(f'BeautifulSoup version:', bs4.__version__)
    
    req = requests.get(url1)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    return req, html, soup

def BeautifulSoup_WebScraping(req, soup):
    """
    Docstring for BeautifulSoup_WebScraping
    """
    
    # finding general info from the page
    headers = req.headers # extract the headers from the page and assign them to a variable 'headers'
    parser = soup.builder.NAME # extract the parser name from the parsed object 'soup', assign it to a variable 'parser'

    print(f'BeautifulSoup is using "{parser}" parser.')
    print(f'\nHeaders: {headers}')
    
    # finding specific info from the page
    first_h2 = soup.find('h2') # find first 'h2' tag inside the parsed object 'soup' and assign it to variable 'first_h2'
    print(f'\nPrimer "h2":', first_h2.text)

    i = 0
    all_h2 = soup.find_all('h2') # extract all 'h2' tag inside parsed object 'soup' and assign it's value to var 'all_h2'
    print(f'\nAll "h2":')
    for h in all_h2: # loop that iterates all 'h2' tags inside variable 'all_h2' and prints each tag text with an index
        i += 1
        print(f'Tag h2 #{i}', h.get_text(strip=True)) # use .get_text to extract only the text from the tags

    # use of attributes of tags to search inside page
    divs = soup.find_all('div', class_='heading-container heading-center')
    #divs_h2 = divs('h2')
    i2 = 0
    print(f'\nAll divs headers:')
    for div in divs:
        i2 += 1
        print(div.get_text(strip=True))
    
    return soup

def image_finding(soup):
    """
    
    """
    
    all_src = soup.find_all(src=True) # find all 'src' link in parsed page 'soup'

    print(f'\nFinding .jpg files:')
    # iterate on var 'all_src' to print each full tag
#    for e in all_src:
#       if e['src'].endswith('.jpg'):
#            print(e)

    for i, image in enumerate(all_src):
        if image['src'].endswith('.jpg'):
            print(image['src'])
            r = requests.get(url1+f'{image["src"]}')

            with open(f'image_{i}.jpg', 'wb') as f:
                f.write(r.content)

def table_finding(soup):
    """
    
    """
    table_url = soup.find_all('iframe')[0]['src']
    print(table_url)

    table_req = requests.get(url1 + table_url)

    table_html = table_req.text
    table_soup = BeautifulSoup(table_html, 'html.parser')
    search_table = table_soup.find('table')

#    print(search_table)

    missing = table_soup.find_all(['th', 'td'], attrs={'style':'color: red;'}) # find missing products using the attribute 'style': 'color: red;'
    #missing_products = [size.text for size in missing]
    missing_products = []
    for size in missing:
        missing_products.append(size.text)

    print()
    print(missing_products)

def name_price_scrape(soup):
    """
    
    """
    divs = soup.find_all('div', class_='detail-box') # find all div tags that have a class = 'detail-box'
    products = [] # create list to store products
    prices = [] # create list to store prices

    try:
        # for loop to iterate the data from variable 'divs' and search all the ones with attribute 'h5' as product and 'h6' as price 
        for div in divs:
            if (div.h6 is not None) and ('Skateboard' in div.h5.text): # if h6 exists and h5 contains the word 'Patineta'
                product = div.h5.get_text(strip=True)
                price = div.h6.get_text(strip=True).replace('$', '')
                # can add filters
                print(f'Product: {product:<17} | price ($): {price}') # print the product (formatting to 16 characters) with it's price
                products.append(product)
                prices.append(price)
    except Exception as e:
        print(f'Error: {e}')
    return products, prices

def mult_page_scrape():
    """
    
    """
    for i in range(1,3):
        url2 = f'{url1}contact{i}'
        print(url2)
        r = requests.get(url2)
        html = r.text
        parse = BeautifulSoup(html, 'html.parser')

        print(parse.h5.text)

def regular_expresions(soup):
    """
    Docstring for regular_expresions
    
    :param soup: Description
    """
    telf = soup.find_all(string=re.compile('\\d+-\\d+-\\d+'))
    print('Phone number:', telf[0])

    copyright = soup.find(string=re.compile('©'))
    first_copyright = copyright.parent.find_next_siblings()
    print(f'\nThis is the copyright:', copyright)
    print('Copyright sibling tag:', first_copyright)

    menu = soup.find(string=re.compile('MENU'))
    print(f'\n"Menu" tag:', menu)
    print('"Menu" parent tag:', menu.parent)
    print('"Menu" next sibling tag:', 
          f'\n{menu.parent.find_next_siblings()}'
          )
    
    print(f'\nAbout exceptions:')
    strings_to_find = ['MENU', 'Carpincho', '©', 'Skateboard']

    for string in strings_to_find:
        try:
            word = soup.find(string=re.compile(string))
            print(word.text)
        except AttributeError:
            print(f'The string "{string}" was not found.')

def data_management(soup, products, prices):
    """
    Docstring for data_management
    
    :param soup: Description
    """
    products.insert(0, 'Products')
    prices.insert(0, 'Prices')
    data = dict(zip(products, prices))
    
    try:
        with open('data.csv', 'w') as f:
            w = csv.writer(f)
            w.writerows(data.items())
        print('File created successfuly!')
    except Exception as e:
        print('File could not be created.', f'\nError: {e}')


def main():
    """
    Call function to use or practice as needed.
    """
    req, html, soup = call_soup()
    products, prices = name_price_scrape(soup)
    
    data_management(soup, products, prices)

if __name__=="__main__":
    main()

