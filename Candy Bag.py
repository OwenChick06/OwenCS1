import random

candy_bag = []
candies_in_bag = 14

for i in range(candies_in_bag):
    candy_bag.append(random.choice(["red","orange","yellow","green","brown","other"]))

reds, oranges, yellows, greens, browns, others =  [],[],[],[],[],[]

for candy in candy_bag:
    if candy == "red":
        reds.append(candy)
    elif candy == "orange":
        oranges.append(candy)
    elif candy == "yellow":
        yellows.append(candy)
    elif candy == "green":
        greens.append(candy)
    elif candy == "brown":
        browns.append(candy)
    elif candy == "other":
        others.append(candy)

print(candy_bag)

print(f'''
reds
oranges
yellows
greens
browns
others:
