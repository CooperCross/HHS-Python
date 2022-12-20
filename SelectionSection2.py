# SelectionSection2.py
# Cooper Cross
# 10/29/19

y = int(input("Please enter a year "))

def isLeap(year):
    if (year % 4 == 0):
        return True
    else:
        return False
    if (year % 100 == 0):
        return False
    else:
        return True
    if(year % 400):
        return True
    else:
        return False




    
print(isLeap(y))
        


    
