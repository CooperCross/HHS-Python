# SquareRootFunction.py
# Cooper Cross
# 10/11/19

def mySqrt(n):
    oldguess = n/2
    for i in range(20):
        newguess = (1/2) * (oldguess + (n/oldguess))
        oldguess = newguess
    return newguess
    
print(mySqrt(999))
