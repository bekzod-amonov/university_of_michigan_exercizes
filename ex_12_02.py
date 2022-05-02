import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
total = 0

address = input('Enter location:')
print('Retrieving', address)
data = urllib.request.urlopen(address, context=ctx).read()

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
rtotal = tree.findall('.//count')
print('Retrieved:', len(data), 'characters')
print('Count:', len(lst))
for item in rtotal:
    print(item.text)
    total = total + int(item.text)
print('Sum:', total)
