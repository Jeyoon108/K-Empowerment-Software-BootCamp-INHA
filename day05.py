# Function
# 함수 원칙 중 하나는 단일 책임의 원칙 때문에 출력을 함수에서 하면 안 된다.

def isprime(n):
    """
    매개변수로 받은 정수가 소수인지 여부를 판정하는 함수
    :param n: integer number
    :return: true or false
    """
    if n <= 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    else:
        return True

help(isprime)
#print(isprime(43))

start = int(input("input start number : "))
end = int(input("input end number : "))

if end < start:
    start, end = end, start

for i in range(start, end+1):
    if isprime(i):
        print(i, end = ' ')
