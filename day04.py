# dictionary

# students = {'name': 'kim inha', 'age': 23, 'eyes': [0.9, 1.1]}
# # for k in students.keys():
# # for k in students:
# # for k in students.values():
# for k, v in students.items():
#     # print(k)
#     print(f'{k} : {v}')
# print(f"이름은 {students['name']}, 나이는 {students['age']}세", end=' ')
# print(f'시력은 좌:{students["eyes"][0]}, 우:{students["eyes"][1]}')

# alcohol dictionary

import random

alcohol_foods = {
    '맥주': '치킨',
    '소주': '회',
    '와인': '치즈',
    '고량주': '유린기'
}
alcohol_list = list(alcohol_foods)  # key값들만 추출
food_list = [food for food in alcohol_foods.values()]  # 밸류 추출, list에 추가 (append)
# print(alcohol_list, food_list)  # 정상적으로 작성됐는지 확인용
while True:
    alcohol = input(f'술을 선택 하세요. 1) {alcohol_list[0]} 2) {alcohol_list[1]} 3) {alcohol_list[2]} 4) {alcohol_list[3]} 5) 아무거나 6) 계산 '
                    f'\n메뉴 입력 : ')
    if alcohol == '6':  # int(input())해서 받으면 그냥 6으로 해놓고 나머지도 숫자로 할 수 있는데 글자로 입력하는 경우도 받아내기 위하여 str으로 코딩 (int로 받으면 글자 입력시 에러가 발생)
        print('계산 완료!')
        break
    elif alcohol == '1':
        print(f'{alcohol_list[0]}에 어울리는 안주는 {alcohol_foods[alcohol_list[0]]}입니다')
    elif alcohol == '2':
        print(f'{alcohol_list[1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[1]]}입니다')
    elif alcohol == '3':
        print(f'{alcohol_list[2]}에 어울리는 안주는 {alcohol_foods[alcohol_list[2]]}입니다')
    elif alcohol == '4':
        print(f'{alcohol_list[3]}에 어울리는 안주는 {alcohol_foods[alcohol_list[3]]}입니다')
#    elif alcohol == '5':
#        print(f'{alcohol_list[random.randint(0,3)]}에 {alcohol_foods[alcohol_list[random.randint(0,3)]]}을(를) 드리겠습니다')
    elif alcohol == '5':
        print(f'{random.choice(alcohol_list)}에 {random.choice(food_list)}을(를) 드리겠습니다.')
    else:
        print('해당하는 번호의 메뉴가 없습니다')
