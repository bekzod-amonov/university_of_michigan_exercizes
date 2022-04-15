total = 0
count = 0
numlist = list()
while True:
    inp = input('Enter numbers: ')
    if inp == 'done': break
        calc = float(inp)
    numlist.append(calc)
        
average = total / count
print("Your result: ", average)
