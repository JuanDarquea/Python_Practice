import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : # secutiry blanket if no input is given
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url) # open the URL
data = uh.read() # read the data from the URL
print('Retrieved',len(data),'characters') # print number of characters retrieved
tree = ET.fromstring(data) # parse the XML data into an ElementTree object

counts = tree.findall('./comments/comment/count') # or comments/comment/count also, .//count works as well.
nums = list() # list to hold all the numbers found
for result in counts: # iterate through each count element
    # Debug print the data :)
    nums.append(int(result.text)) # append the integer value of the text to the list
#    print(result.text)

print('Count:', len(nums)) # print the count of numbers found
print('Sum:', sum(nums)) # print the sum of the numbers found
