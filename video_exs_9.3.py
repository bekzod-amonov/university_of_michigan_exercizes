# jrfheig orgh erog rg herog hg ireoh ergerg erjg e ergi eo ergj erioerg erog erg erlgh erghegpowjgpeirgh erpgeirogh;se eshg eo;ihh edbndl;fbhdb dsflhj dlndfklh sdflhndfjhgndfg sdlfhjdslhn sdflh dsfhj''pdsh js dfjd;fjhkdfhj

counts = dict()
print('Enter a line text:')
line = input('')
words = line.split()
print("Words: ", words)

for word in words:
    counts[word] = counts.get(word,0) + 1
print(counts)
