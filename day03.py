# prime number

number = int(input("input number : "))
counts = 0

i = 1

# while i <= number:
#     if number % i == 0:
#         counts += 1
#     i += 1
# if counts == 2:
#     print(f'{number} is a prime number!')
# else:
#     print(f'{number} is not a prime number!')


# for i in range(1,number + 1):
#     if number % i == 0:
#         counts += 1
# if counts == 2:
#     print(f'{number} is a prime number!')
# else:
#     print(f'{number} is not a prime number!')



# for i in range(2, number):
#     if number % i == 0:
#         counts += 1
# if counts:
#     print(f'{number} is not a prime number!')
# else:
#     print(f'{number} is a prime number!')


# for i in range(2, number):
#     if number % i == 0:
#         counts += 1
# if counts:
#     print(f'{number} is not a prime number!')
# else:
#     print(f'{number} is a prime number!')

is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
    print(i)

if is_prime:
    print(f'{number} is a prime number!')
else:
    print(f'{number} is not a prime number!')