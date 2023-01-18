# closures

def calculate():
    x = 1
    y = 2
    temp = 0

    def add_sub(n):
        # nonlocal temp  # 지역 변수를 전역 변수로 바꿀 수 있다.
        temp = 0  # nonlocal temp로 했을 때와 다른 결과를 도출한다.
        # x = 11  # local variable (지역 변수)
        temp = temp + x + n - y
        return temp

    return add_sub


c1 = calculate()  # 외부의 함수를 모두 실행한 후 return이 add_sub이므로 외부의 내용을 기억 한채로 closure 역할을 한다.
for i in range(5):
    print(c1(i))

print(type(c1))
print(c1)  # calculate의 add_sub이라는 족보(클로저임)를 나타냄
