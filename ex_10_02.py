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












    
