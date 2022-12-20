# Stop.py
# Cooper Cross
# 1/22/2020

def stop():
    dec = input("Do you want to continue? ").lower()
    if dec == "s" or dec == "stop":
        print("Program Stopped.")
    else:
        stop()

stop()
