counts = dict()
names = ['Abror','Umid','Atham','Sanjar','Sherzod','Doniyor',
        'Abror','Sardor','Anvar','Atham','Umid','Sherzod','Doniyor']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#alternative method

#for name in names:
#    counts[name] = counts.get(name,0) + 1
#print(counts)
