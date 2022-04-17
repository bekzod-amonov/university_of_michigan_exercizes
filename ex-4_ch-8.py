
#works with mbox-short.txt file
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
