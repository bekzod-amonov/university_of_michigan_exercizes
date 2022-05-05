***************************** Python for Everybody --> Using Python to Access Web Data --> WEEK1 - Getting Started **********************************************
***************************** Python for Everybody --> Using Python to Access Web Data --> WEEK2 - Regular Expressions (Chapter 11) **********************************

#Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
#Data Files
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#    Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#    Actual data: http://py4e-data.dr-chuck.net/regex_sum_57123.txt (There are 49 values and the sum ends with 560)
#These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
#Handling The Data
#The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers. 
"""
import re
#numbers = []
total = 0
fname = input("Enter file:")
if len(fname) < 1 : fname="regex_sum_42.txt"
handle = open(fname)
for line in handle:
    numbers = re.findall("[0-9]+",line)
    if not numbers: continue
    else:         
        for num in numbers:
            total = total + int(num)
print(total)

(METHOD 2) Python 3:
import re
print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )

***************************** Python for Everybody --> Using Python to Access Web Data --> WEEK3 - WNetworks and Sockets (Chapter 12) **************************














***************************** Python for Everybody --> Using Python to Access Web Data --> WEEK4 - Programs that Surf the Web (Chapter 12)************************

***************************** Python for Everybody --> Using Python to Access Web Data --> WEEK5 - Web Services and XML (Chapter 13)************************

import xml.etree.ElementTree as ET
input = '''
<stuf>
    <users>
        <user x ='2'>
            <id>001</id>
            <name>Bekzod</name>
        </user>
        <user x='7'>
            <id>009</id>
            <name>Sherzod</name>
        </user>
    </users>
</stuf> '''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('ID', item.find('id').text)
    print('Attribute', item.get('x'))

***************************** Python for Everybody --> Using Python to Access Web Data --> WEEK6 - JSON and the REST Architecture (Chapter 13) ************************
