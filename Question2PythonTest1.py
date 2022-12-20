# Question2PythonTest1.py
# Cooper Cross
# 10/8/19

names = ["Kaitlyn", "Joel", "Derya", "Jonathan", "Hannah", "Ian"]
s = 15
print("First Name".rjust(s))
for i in range(s):
    print("-",end="")
print()
for name in names:
    print(name.rjust(s))
