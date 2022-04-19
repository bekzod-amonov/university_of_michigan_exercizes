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
