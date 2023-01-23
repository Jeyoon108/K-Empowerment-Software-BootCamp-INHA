# A to Z reminding

# Ch4 practice #2
import random

small = random.choice([True, False])
green = random.choice([True, False])

if small:
    if green:
        print("It's a pea")
    else:
        print("It's a cherry")
else:
    if green:
        print("It's a watermelon")
    else:
        print("It's a pumpkin")
