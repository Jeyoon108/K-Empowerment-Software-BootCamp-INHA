# class

# class Pokemon:
#     def __init__(self):  # 객체 생성 시 동작
#         print("포켓몬 객체 생성됨")
#
#
# p1 = Pokemon()
# p2 = Pokemon()
# print(p1, p2)  # 서로 다른 메모리 주소를 가진다.

class Pokemon:
    def __init__(self, name, owner, skills):  # 객체 생성 시 동작 # skill을 구현할 때 스킬이 하나가 아니니 자료구조를 준비한다 (만만한게 리스트)
        self.name = name
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 {name} 생성됨")


    def info(self):  # 멤버 함수
        print(f"{self.owner}의 포켓몬은 {self.name}입니다")
        for skill in self.skills:
            print(skill)


p1 = Pokemon('피카츄', '지우', '50만 볼트/100만 볼트/번개')
p2 = Pokemon('꼬부기', '오박사', '고속 스핀/물대포/몸통박치기/할퀴기')
# print(p1, p2)  # 서로 다른 메모리 주소를 가진다.
print(p1.name)
print(p2.name)
# print(f"{p1.owner}의 포켓몬은 {p1.name}입니다")
# print(f"{p2.owner}의 포켓몬은 {p2.name}입니다")
p1.info()
p2.info()
# print(p2.skills)
