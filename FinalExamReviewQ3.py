# FinalExamReviewQ3.py
# Cooper Cross
# 1/15/2020

def that():
    dec = input("Do you want to continue? ").lower()
    if dec == "no" or dec == "n":
        print("That's all, folks!")
    else:
        that()
            
that()
