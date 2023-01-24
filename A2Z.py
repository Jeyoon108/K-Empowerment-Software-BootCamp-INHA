# A to Z reminding

# Ch9 practice recursion

def fib(n):
    """
    피보나치 수열
    :param n: f(n)
    :return: 1 or fib(n-1) + fib(n-2)
    """
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(8))
