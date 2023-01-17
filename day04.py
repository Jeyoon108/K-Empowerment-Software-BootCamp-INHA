# list

# primes = [2, 19, 3.0, 5, 7, 11]
# primes_sorted = sorted(primes)
# print(primes)
# print(primes_sorted)

# mixed = ['6', '4', '5', 'A', '7', '강아지', 'Bow wow', 'b', '제윤']
# mixed.sort(reverse=True)
# print(mixed)

# a = [1, 2, 3]
# b = a
# print(b)
# a[0] = 'surprise'
# print(a, b)
# b[0] = 'nope'
# print(a, b)

# a = [1, 2, 3]
# b = a.copy()
# c = list(a)
# d = a[:]
# e = a
# a[2] = 'sw'
# print(a, b, c, d, e)

# deepcopy()
import copy

a = [1, 2, [5, 9]]
b = a.copy()
c = list(a)
d = a[:]
e = copy.deepcopy(a)
a[2][1] = 'wow'
print(a, b, c, d, e)
