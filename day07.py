# class - inheritance

# class Pokemon:
#     def __init__(self):  # 객체 생성 시 동작
#         print("포켓몬 객체 생성됨")
#
#
# p1 = Pokemon()
# p2 = Pokemon()
# print(p1, p2)  # 서로 다른 메모리 주소를 가진다.

class Pokemon:
    def __init__(self, owner, skills):  # 객체 생성 시 동작 # skill을 구현할 때 스킬이 하나가 아니니 자료구조를 준비한다 (만만한게 리스트)
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 생성:", end=' ')


    def info(self):  # 멤버 함수
        print(f"{self.owner}의 포켓몬이 사용 가능한 스킬")
        for skill in self.skills:
            print(skill)


    def attack(self, idx):
        print(f'{self.skills[idx]} 스킬 시전!')



class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  # 부모 calss 호출할 때 쓰는 것
        self.name = "피카츄"
        print(f"{self.name}")


    def attack(self, idx):  # override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} (번개 속성) 스킬 시전!')


# class Ggoboogi(Pokemon):  # inheritance
#     def __init__(self, owner, skills):
#         super().__init__(owner, skills)  # 부모 calss 호출할 때 쓰는 것
#         print(f"꼬부기")

class Ggoboogi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  # 부모 calss 호출할 때 쓰는 것
        self.name = "꼬부기"
        print(f"{self.name}")


    def attack(self, idx):  # override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} (물 속성) 스킬 시전!')


    def swim(self):
        print(f'{self.name}가 수영을 합니다')


p0 = Pokemon('웅이', '어떤공격')
p0.attack(0)
# p0.swim()  # 꼬부기 클래스의 객체들이 사용할 수 있는 고유 메서드
pk1 = Pikachu('지우', '전광석화/10만 볼트/전기쇼크/번개')
# pk1.info()
ggo1 = Ggoboogi('오박사', '거품/물대포/몸통박치기/껍질에숨기')
# ggo1.info()
ggo1.swim()
pk1.attack(3)
ggo1.attack(0)

# pi1.info()
# p1 = Pokemon('웅이', '스핀 테일/브레스/몸통박치기')
# p2 = Pokemon()
