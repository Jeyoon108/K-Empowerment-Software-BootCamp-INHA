# while문 사용하여 구구단 만들기
#
# dan = int(input('Dan : '))
# i = 1
#
# while i < 10:
#     #print(f'{dan} * {i} = {dan * i}')
#     print('{0} * {1} = {2}'.format(dan, i, dan * i))
#     i += 1

# 1~9단만 사용할 수 있게, 틀릴시 다시 진행

# while True:
#     dan = int(input('Dan : '))
#
#     if 1 < dan < 10:
#         i=1
#         while i < 10:
#             print('{0} * {1} = {2}'.format(dan, i, dan * i))
#             i += 1
#         break
#     else:
#             print('2에서 9사이의 값을 입력하세요')

# while True:
#     stuff = input("String to capitalize [type q to quit]: ")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())

# numbers = [1, 10, 5]
# position = 0
# while position < len(numbers):
#     number =numbers[position]
#     if number % 2 == 0:
#         print('Found even number', number)
#         break
#     position += 1
# else:
#     print('No even number found')
