# Function
import random


# def buggy(arg, result=[]):
#     result.append(arg)
#     print(result)
#
#
# result_1 = ['A']
# result_1 = []
# print(result_1)
# buggy('a')
# buggy('b')

# V0.2  # 인원 수 입력하면 알아서 어른 수, 아이 수 계산, 총 금액 계산 코딩해보기
import random

def calculate_fee(args)-> list:  # * 사용할 때 관용적으로 변수의 이름은 args를 사용한다. 핵심은 던져진 인수의 개수를 예측할 수 없을 때 사용됨 + ->list는 타입힌트 (없어도 되는데 타입 알려줌)
    """
    놀이공원 요금 계산 프로그램
    :param args: ages in list
    :return: [전체 인원 수, 어른 수, 아이 수, 지불할 총 입장료]
    """
    total = 0
    adults = 0
    kids = 0
    for age in args:
        if 19 <= age:  # adult
            total = total + 10000
            adults = adults + 1
        else:
            total = total + 3000
            kids = kids + 1
    return [len(args), adults, kids, total]


no_of_visitor = int(input('몇 분이세요? '))
ages = [random.randint(1, 60) for age in range(no_of_visitor)]
results = calculate_fee(ages)
print(f'{results[0]}명 방문 하셨고 어른 {results[1]}명, 아이 {results[2]}명 총 요금은 {results[-1]}원 입니다')
print(f'일행분들의 나이는 {ages}세 입니다.')

# ㅇ분 방문하셨고 어른 ㅇ명 아이 ㅇ명 총 요금은 ㅇ원 입니다. 형식

# print(calculate_fee(20, 20, 25))
# print(calculate_fee(45, 43, 10,7))