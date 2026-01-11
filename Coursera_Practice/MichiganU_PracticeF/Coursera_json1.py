import json

def dict_json():
    
    data = '''
    {
      "name" : "Chuck",
      "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
      },
      "email" : {
        "hide" : "yes"
      }
    }'''

    try:
        info = json.loads(data)
    except Exception as e:
        print(f'Error: {e}')

    print('Name:', info['name'])
    print('Hide:', info["email"]["hide"])


def list_json():
    """
    Docstring for list_json
    """
    inp = '''
    [
      { "id" : "001",
        "x" : "2",
        "name" : "Chuck"
      } ,
      { "id" : "009",
        "x" : "7",
        "name" : "Chuck"
      }
    ]'''

    info = json.loads(inp)
    print('User count:', len(info))
    
    try:
        for i, item in enumerate(info, 1):
            print(f'Input {i}')
            print('Name:', item['name'])
            print('ID:', item['id'])
            print('Attribute:', item['x'])
            print()
    except Exception as e:
        print('Error:', e)

def main():
    """
    Docstring for main
    """
    print('Example with one json object:')
    dict_json()
    print('-'*50)
    print('Example with two json objects:')
    list_json()


if __name__ == '__main__':
    main()
