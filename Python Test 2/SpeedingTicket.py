# SpeedingTicket.py
# Cooper Cross
# 11/22/19

import random

mphOver = -1
while mphOver <= 0:
    mphOver = int(input("Amount in MPH above speed limit: "))


if mphOver >= 31:
    print("Your suggested fine is:",100 + random.randint(100, 200))
    
elif mphOver >= 21 and mphOver <= 30:
    print("Your suggested fine is:",70)
    
elif mphOver >= 11 and mphOver <= 20:
    print("Your suggested fine is:",40)
    
else:
    print("Your suggested fine is:",20)
