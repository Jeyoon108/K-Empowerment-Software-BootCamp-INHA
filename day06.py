# generator

def a():  # generator
    yield 1
    yield 2
    yield 3


def b():  # normal function
    return 1  # stop iteration
    return 2
    return 3


print(a(), b())  # 이 때 a값을 뽑으려면 for문을 돌려야함
c = a()
print(c)
for i in c:
    print(i)
