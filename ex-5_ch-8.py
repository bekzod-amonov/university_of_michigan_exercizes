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
