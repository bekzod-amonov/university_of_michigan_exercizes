import xml.etree.ElementTree as ET
data = ''' <person>
    <name>Bekzod</name>
    <phone type='intl'>+998996400501</phone>
    <email hide='yes'>bekzod.amonov@gmail.com</email>
</person> '''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
