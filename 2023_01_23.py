# A to Z reminding

# Ch6 practice # 2
import random

guess_me = random.randint(1, 10)
number = random.randint(1, 10)
# guess_me = 7
# number = 1
print(f'number : {number}, guess number : {guess_me}')

while True:
    if number == guess_me:
        print('found it!')
        break
    elif number < guess_me:
        print(f'too low, number is {number}')
        number += 1
    else:
        print('oops')
        break
