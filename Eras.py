# Eras.py
# Cooper Cross
# 11/20/19

year = float(input("How many millions of years ago is it: "))

if year >= 257.17:
    print("Unknown Era")
    
elif year < 257.17 and year >= 66:
    print("Mesozoic Era")

else:
    print("Cenozoic Era")
