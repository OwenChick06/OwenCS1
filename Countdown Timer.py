import time

try:
    countdown = int(input("How long to count? "))
    orig_countdown = countdown
    cycle = int(input("How many times to count? "))

    cycle = cycle - 1

    while cycle >= 0:
        time.sleep(1)
        countdown -= 1
        print(countdown + 1)
        if countdown == 0:
            countdown = orig_countdown
            cycle -= 1
    print("done")     
        
except ValueError:
    print("That is not a number")