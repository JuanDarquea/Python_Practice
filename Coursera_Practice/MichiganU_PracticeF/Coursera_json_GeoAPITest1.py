from urllib import request, parse
import json

def get_pattern():
    try:
        url_pattern = input('Enter location: ')
        if len(url_pattern) < 1: raise NameError
    except NameError:
        print('Location not selected.')
        url_pattern = 'South Federal University'

    if url_pattern == 'break':
        quit()

    return url_pattern

def location_pattern(url_pattern):
    """

    """
    service_url = 'http://py4e-data.dr-chuck.net/opengeo?'
    try:
        url_pattern = url_pattern.strip()
        params = dict()
        params['q'] = url_pattern
    except Exception as e:
        print('Error:', e)

    full_url = service_url + parse.urlencode(params)

    print('Retrieving url:', full_url)
    try:
        req = request.urlopen(full_url)
        data = req.read().decode()
    except Exception as e:
        print('Error:', e)

    print(f'Retrieved {len(data)} characters.')

    return data

def result(data):
    """

    """
    while True:
        try:
            js = json.loads(data)
        except:
            None

        if not js or 'features' not in js:
            print('-'*20, 'Download Error!')
            print(data)
            break

        if len(js['features']) == 0:
            print('-'*20, 'Object not found')
            print(data)
            break

        plus_code = js['features'][0]['properties']['plus_code']
        print('Plus code:', plus_code)
        return main()

def main():
    """

    """
    pattern = get_pattern()
    data = location_pattern(pattern)
    result(data)

if __name__=="__main__":
    main()
