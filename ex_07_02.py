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
print("Average spam confidence: ", taver)
