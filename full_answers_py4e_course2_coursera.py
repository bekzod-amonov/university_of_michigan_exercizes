***************************** Python for Everybody --> Python Data Structures --> WEEK1 - Strings **********************************************

#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
slc = text.find('0')
slc_fl = float(slc)
ans = text[slc:slc+6]
print(ans)

***************************** Python for Everybody --> Python Data Structures --> WEEK2 - Installing and Using Python  **********************************************

***************************** Python for Everybody --> Python Data Structures --> WEEK3 - Files **********************************************

#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. 
#Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

# Use words.txt as the file name
fname = input("Enter file name: ")
fnames = open(fname)
for line in fnames:
    linex = line.rstrip()
    print(linex.upper())
    
#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
ftotal = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    averf = float(line[-7:-1])
    count = count + 1  
    ftotal = ftotal + averf
    
taver = ftotal / count
print("Average spam confidence:", taver)

***************************** Python for Everybody --> Python Data Structures --> WEEK4 - Lists **********************************************

#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words 
#using the split() method. The program should build a list of words. For each word on each line check to 
#see if the word is already in the list and if not append it to the list. When the program completes, sort 
#and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    words = list(line.rstrip().split())
    for element in words:
        if element in lst:
            continue   
        else:
            lst.append(element)
lst.sort()
print(lst)

#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent 
#the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = input("Enter file name: ")
fh = open(fname)
count = 0

if len(fname)<1:
	fname = mbox-short.txt

for line in fh:
    if line.startswith("From "):
        splitter = line.split()
        print(splitter[1])
        count = count + 1
print('There were' ,count, 'lines in the file with From as the first word')

***************************** Python for Everybody --> Python Data Structures --> WEEK5 - Dictionaries **********************************************

#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program 
#creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
fh = open(fname)
counts = dict()
lst = list()
largestnum = None
largestval = None
for word in fh:
    if word.startswith('From '):
        wordss = word.rstrip()
        words = wordss.split()
        nwords = words[1]
        lst.append(nwords)

for element in lst:
    counts[element] = counts.get(element,0) + 1

for key,value in counts.items():
    if largestnum is None or value > largestnum:
        largestnum = value
        largestval = key
print(largestval, largestnum)

***************************** Python for Everybody --> Python Data Structures --> WEEK6 - Tuples **********************************************

#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day 
#for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then 
#splitting the string a second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
handle = open(name)
lst = list()
count = dict()

for word in handle:
    if word.startswith("From "):
        words = word.split()
        nwords = words[5]
        spwords = nwords.split(':')
        finwords = spwords[0]
        lst.append(finwords)

for counter in lst:
    count[counter] = count.get(counter, 0) + 1
    
#lst2 = sorted([(k,v) for k,v in count.items()])
#print(k,v)

for (key, value) in sorted(count.items()):
    print(key, value)
    
***************************** Python for Everybody --> Python Data Structures --> WEEK7 - Graduation **********************************************
