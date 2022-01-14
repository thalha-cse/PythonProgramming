# This project is countdown timer, which is usually we have seen in our camera, after timer completed it takes a pic
# This project contains a module name time, used a function, while loop etc..

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\n")
        time.sleep(1)
        t -= 1
    print('Timer Completed')

t = int(input("Enter the time in seconds:- "))

countdown(t)
