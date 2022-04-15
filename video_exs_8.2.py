total = 0
count = 0
while True:
    calcraw = input('Enter numbers: ')
    if calcraw == 'done':
        break
    else:
        calc = float(calcraw)
    count = count + 1
    total = total + calc
average = total / count
print("Your result: ", average)
