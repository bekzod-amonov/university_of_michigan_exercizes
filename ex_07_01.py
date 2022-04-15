# Use words.txt as the file name
fname = input("Enter file name: ")
fnames = open(fname)
for line in fnames:
    linex = line.rstrip()
    print(linex.upper())
