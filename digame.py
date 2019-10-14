import random

turns = 5
i = 0
while i <= turns:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1 == dice2:
        turns = turns + 1
    print(dice1,dice2)
    i = i+1

#if I roll a double i get an extra turn (+1)
