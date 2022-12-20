# RecursionPractice.py
# Cooper Cross
# 12/17/19

def findFactorial(start,counter):
    factorial = start
    print()
    for i in range(start-1,0,-1):
        factorial = factorial * i
        print(str(factorial),end = "\t")
    if start > 0: #base case
        counter += 1
        findFactorial(start-1,counter) #recursive call
        print(str(factorial) + "\t" + str(counter))

beginNumber = int(input("Enter starting number: "))
counter = 0
findFactorial(beginNumber,counter)

### Prints total w/o setting total back to 0
##def addNumbers(start,total,counter):
##    print()
##    for i in range(start,0,-1):
##        total += i #total = total + i
##        print(str(total), end = "\t")
##    if start > 0: #base case
##        counter += 1
##        addNumbers(start - 1,total,counter) #recursive call
##        print(str(total) + "\t" + str(counter))
##
##beginNumber = int(input("Input a starting number: "))
##total = 0
##counter = 0
##addNumbers(beginNumber,total,counter)

### Prints sum each time through loop
##def addNumbers(start):
##    total = 0
##    print()
##    for i in range(start,0,-1):
##        total += i #total = total + i
##        print(str(total), end = "\t")
##    if start > 0: #base case
##        addNumbers(start - 1) #recursive call
##        print(str(total))
##
##beginNumber = int(input("Input a starting number: "))
##addNumbers(beginNumber)

# Prints numbers recursively

##def printNumber(beginNumber):
##    print()
##    for i in range(beginNumber,0,-1):
##        print(str(i),end = "\t")
##    if(beginNumber - 1 >= 0): # base case
##        printNumber(beginNumber - 1) # recursive call
##
##number = int(input("Input a number: "))
##
##printNumber(number)

