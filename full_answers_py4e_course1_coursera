***************************** Python for Everybody --> Programming for everybody --> WEEK1 - WELCOME **********************************************
***************************** Python for Everybody --> Programming for everybody --> WEEK2 - INSTALLING PYTHON - OVERVIEW **********************************************
***************************** Python for Everybody --> Programming for everybody --> WEEK3 - WHY WE PROGRAMM  **********************************************
***************************** Python for Everybody --> Programming for everybody --> WEEK4 - Variables and Expressions **********************************************
***************************** Python for Everybody --> Programming for everybody --> WEEK5 - Conditional Code **********************************************

#3.1 Write a program to prompt the user for hours and rate per hour
#using input to compute gross pay. Pay the hourly rate for the hours
#up to 40 and 1.5 times the hourly rate for all hours worked above
#40 hours. Use 45 hours and a rate of 10.50 per hour to test the
#program (the pay should be 498.75). You should use input to read
#a string and float() to convert the string to a number. Do not
#worry about error checking the user input - assume the user types numbers properly.


hrs = input("Enter Hours:")
rate = input("Enter rate:")
h = float(hrs)
r = float(rate)
if h==40:
    print(h * r)
if h>40:
    print((((h-40)*1.5)+40)*r)

#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score
#is out of range, print an error. If the score is between 0.0 and 1.0, print
#a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message
#and exit. For the test, enter a score of 0.85.

while True:
    line_raw = input('Enter a range between 0 and 1: ')
    if line_raw == 'done':
        break
    try:
        line = float(line_raw)
        if line >= 0.9:
            print('A')
        elif line >= 0.8:
            print('B')
        elif line >= 0.7:
            print('C')
        elif line >= 0.6:
            print('D')
        elif line < 0.6:
            print('F')
    except:
        print('Out of range')
        exit()

***************************** Python for Everybody --> Programming for everybody --> WEEK6 - Functions **********************************************

#4.6 Write a program to prompt the user for hours and rate per hour
#using input to compute gross pay. Pay should be the normal rate for
#hours up to 40 and time-and-a-half for the hourly rate for all hours
#worked above 40 hours. Put the logic to do the computation of pay
#in a function called computepay() and use the function to do the
#computation. The function should return a value. Use 45 hours and
#a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use input to read a string and float() to convert the string
#to a number. Do not worry about error checking the user input unless
#you want to - you can assume the user types numbers properly. Do not
#name your variable sum or use the sum() function.

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

fh = float(hrs)
fr = float(rate)

def computepay(fh, fr):
    if fh > 40:
        pay = (fh-40)*(fr*1.5) + 40*fr
    else:
        pay = fr * fh
    return pay

payroll = computepay(fh, fr)
print("Pay", payroll)

**************************** Python for Everybody --> Programming for everybody --> WEEK7 - Loops and Iterations **********************************************

#5.2 Write a program that repeatedly prompts a user for
#integer numbers until the user enters 'done'. Once 'done'
#is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it
#with a try/except and put out an appropriate message and ignore
#the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
    inp = input('Enter a number: ')
    if inp == "done":
        break
    try:
        inp_data = int(inp)
        if largest is None or largest < inp_data:
            largest = inp_data
        if smallest is None or smallest > inp_data:
            smallest = inp_data
    except ValueError:
         print('Invalid input')
         continue
print('Maximum is', largest)
print('Minimum is', smallest)














