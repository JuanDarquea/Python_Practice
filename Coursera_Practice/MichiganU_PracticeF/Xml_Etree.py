import xml.etree.ElementTree as ET

def example1():
    data = '''<person>
        <name>Chuck</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>'''

    tree = ET.fromstring(data)
    print('-'*10, 'Xml Example 1', '-'*10)
    print('Name:', tree.find('name').text)
    print('Phone:', tree.find('phone').text.strip())
    print('Email "hide" attribute:', tree.find('email').get('hide'))
    print()

def example2():
    data = '''<stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>
    </stuff>'''

    tree = ET.fromstring(data)
    print('-'*10, 'Xml Example 2', '-'*10)
    users = tree.find('users')
    print('User count:', len(users.findall('user')))
    for user in users.findall('user'):
        print(' ID:', user.find('id').text)
        print(' Name:', user.find('name').text)
        print(' User "x" attribute:', user.get('x'))
        print()
    print()

def example3():
    data = '''<stuff>
        <users>
            <user x="2">
                <id type="intl">001</id>
                <name type="str">Chuck</name>
            </user>
            <user x="7">
                <id type="intl">009</id>
                <name type="str">Brent</name>
            </user>
        </users>
    </stuff>'''

    tree = ET.fromstring(data)
    print('-'*10, 'Xml Example 3', '-'*10)
    lst = tree.findall('users/user')
    print('User count:', len(lst))
    for item in lst:
        print('User attribute "x":', item.get('x'))
        print(' Name:', item.find('name').text)
        print(' Name attribute "type":', item.find('name').get('type'))
        print(' ID:', item.find('id').text)
        print(' ID attribute "type":', item.find('id').get('type'))
        print()
    print()

def main():
    example1()
    example2()
    example3()

if __name__ == '__main__':
    main()