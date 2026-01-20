from urllib import request, parse
#from urllib import request
import requests
import http, json, ssl

service_url = 'https://py4e-data.dr-chuck.net/opengeo?'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    try:
        address = input('Enter location: ')
        if len(address) < 1: 
            print('Goodbye!')
            break
    except Exception as e:
        (f'Error: {e}')

    try:
        address = address.strip()
        params = dict()
        params['q'] = address
    except Exception as e:
        print('Error:', e)

    try:
        url = service_url + parse.urlencode(params)
    except TypeError:
        print('File type incorrect.')
    except NameError:
        print('File name incorrect.')

    print('Retrieving URL: ', url)
    try:
        uh = request.urlopen(url, context=ctx)
        data = uh.read().decode()
    except NameError:
        print('Cannot read file.')
    print('Retrieved', len(data), 'characters', data[:28].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('-'*20, 'Error downloading json file.', '-'*20)
        print(data)
        break
    
    if len(js['features']) == 0:
        print('-'*20, 'Object not found.', '-'*20)
        print(data)
        break

    #print(json.dumps(js['features'][0], indent=4)) # for reference of whole json file
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']

    print('lat -', lat, f'\nlon -', lon)
    location = js['features'][0]['properties']['formatted']
    plus_code = js['features'][0]['properties']['plus_code']
    print('Address:', location)
    print('Plus code:', plus_code) 
