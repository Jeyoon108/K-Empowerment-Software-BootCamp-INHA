# Function

def answer():
    """
    숫자 출력 함수
    :return:
    """
    print(60)


def call_func(f):
    """
    매개변수로 함수를 넘겨 받아 실행
    :param f: 매개변수가 함수인 함수
    :return:
    """
    f()  # 넘겨 받은 함수 실행


def subtract(n1, n2):
    print(n1 - n2)


def run_func(f, arg1, arg2):
    """
    함수를 매개 변수로 받아 함수 안에서 해당 함수를 실행
    :param f: 첫 번째 인수는 함수
    :param arg1: 정수 값
    :param arg2: 정수 값
    :return:
    """
    f(arg1, arg2)


a = (5, 7, -11)
print(sum(a))


# run_func(subtract, 99, 88)
#
# call_func(answer)
# print(type(call_func))
