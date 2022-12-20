# -----------------------------------------+
# Cooper Cross                             |
# Business Card Program Part II            |
# Last Updated: September 20, 2019         |
# -----------------------------------------|
# Same as the business card program I, but |
# the user is prompted to give a first and |
# last name, e-mail, and phone number, and |
# that information is displayed instead of |
# preset information                       |
# -----------------------------------------+

f = input("Enter your first name: ")
f = str(f)
l = input("Enter your last name: ")
l = str(l)
p = input("Enter your phone number in (xxx)xxx-xxxx format: ")
p = str(p)

print(" ")
print("Here is your buiness card")
print(" ")

print("+------------------------------------------------+")
print("|    |\t\t\t\t\t\t |")
print("|   -|\t\t"+(l+", "+f).ljust(22)+"\t\t |")
print("|  --|\t\tTribute Liabilities Associate\t |")
print("| ---|\t\tParasail Capital\t\t |")
print("| ---------\t\t\t\t\t |")
print("|  -------\t4 Hunger Plaza\t\t\t |")
print("|\t\tSTE 1400\t\t\t |")
print("|\t\tDistrict 12, Panem 00012\t |")
print("|\t\t\t\t\t\t |")
print("| Work:"+(p+" @: "+f).lower().ljust(21)+"@parasail.com\t |")
print("+------------------------------------------------+")
