# LiftTicket.py
# Cooper Cross
# 12/3/19

def create_ski_day_budget():
    budget = int(input("Enter your budget: "))
    total = purchase_lift_ticket(budget)
    if total >= 0:
        print("You have stayed in budget: ")
        print("Your final total is:"+str(total))
    else:
        print("You have exceeded your budget")
        print("Your final total is:"+str(total))

def purchase_lift_ticket(budget):
    dayLength = input("Length of your stay: ")
    age = int(input("Enter your age: "))
    half = 1
    full = 2
    if age <= 17:
        ticketPrice = 30
    if age >= 17 and age < 65:
        ticketPrice = 45
    if age >= 65:
        ticketPrice = 30
    if dayLength == full:
        ticketPrice=int(ticketPrice)
    if dayLength == half:
        ticketPrice = ticketPrice/2
    ticketPrice= ticketPrice * 1.05
    total = budget - ticketPrice
    return total

create_ski_day_budget()
    
