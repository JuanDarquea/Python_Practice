from urllib import request
import json

url = input('Enter location: ')
if url == '':
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print(f'\nRetrieving:', url)
def get_url(url):
    """
    
    """
    try:
        get_url1 = request.urlopen(url)
        data = get_url1.read().decode()
        count = len(data)
        print(f'Retrieved {count} characters.')
    except NameError:
        print('Url could not be retrieved.')
    except Exception as e:
        print(f'Error: {e}')

    return data 

def file_json(data):
    """
    
    """
    print('\nReading url json:')
    try:
        file = json.loads(data)
        print('Data successfully read')
    except Exception as e:
        print('Error:', e)

    #print(json.dumps(file['comments'][0], indent=4)) # debug print to certify data inside json

    # commment count
    comments = file['comments']
    count = 0
    comm = 0
    for c in comments:
        count += 1
        comm += int(c['count'])

    print('Count:', count)
    print('Sum:', comm)

def main():
    """
    Main function that calls the needed functions for the program to work.
    """

    data = get_url(url)
    file_json(data)

if __name__=="__main__":
    main()
