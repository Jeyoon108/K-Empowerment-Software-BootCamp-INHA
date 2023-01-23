# A to Z reminding

# Ch6 practice # 3
import random
guess_me = random.randint(0, 9)
print(guess_me)

for number in range(10):
    if number < guess_me:
        print(f'too low, {number}')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
