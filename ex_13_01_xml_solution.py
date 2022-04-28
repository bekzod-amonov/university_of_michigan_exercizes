import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

location = input('Enter location:')

str = ET.fromstring(input)
lst = str.findall('comments/comment')
print('Count:', len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('Count:', item.find('count').text)
