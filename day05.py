# Function

# def do_nothing():
#     pass
#
#
# mamamoo = ['화사', '솔라', '휘인', '문별']
#
# #print(mamamoo.pop())  # 삭제할 값 리턴 후 삭제
# print(mamamoo.remove('문별'))  # 해당 요소 삭제, 값 리턴하지 않으므로 None 출력됨
# print(mamamoo)

# do_nothing()
# print(do_nothing())

def calculate_fee(*args):  # * 사용할 때 관용적으로 변수의 이름은 args를 사용한다. 핵심은 던져진 인수의 개수를 예측할 수 없을 때 사용됨
    """
    놀이공원 요금 계산 프로그램
    :param args: ages
    :return: 지불할 총 입장료
    """
    total = 0
    for age in args:
        if 19 <= age:  # adult
            total = total + 10000
        else:
            total = total + 3000
    return total


print(calculate_fee(20, 20, 25))
print(calculate_fee(45, 43, 10, 7))