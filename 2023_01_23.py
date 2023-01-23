# A to Z reminding

# mutable, immutable
z = {'A': 'a', 'B': 'b', 'C': 'c'}
x = z
z['A'] = '이거'
print(z)
print(x)

# Ch4 practice
import random

secret = random.randint(1, 10)
guess = random.randint(1, 10)

if guess < secret:
    print(f'gusee: {guess}, secret: {secret} \ntoo low')
elif guess > secret:
    print(f'gusee: {guess}, secret: {secret} \ntoo high')
else:
    print(f'gusee: {guess}, secret: {secret} \njust right')
