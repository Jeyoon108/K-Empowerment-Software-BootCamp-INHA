# game - 중복코드 제거, getter/setter - > property -> decorator
# __hiddenfield

# class Pokemon:
#     def __init__(self):  # 객체 생성 시 동작
#         print("포켓몬 객체 생성됨")
#
#
# p1 = Pokemon()
# p2 = Pokemon()
# print(p1, p2)  # 서로 다른 메모리 주소를 가진다.

class Pokemon:
    count = 0
    def __init__(self, owner, skills):  # 객체 생성 시 동작 # skill을 구현할 때 스킬이 하나가 아니니 자료구조를 준비한다 (만만한게 리스트)
        self.__hidden_owner = owner  # like private
        self.skills = skills.split('/')
        print(f"포켓몬 생성:", end=' ')
        Pokemon.count += 1

    @property
    def owner(self):
        return self.__hidden_owner
    @owner.setter
    def owner(self, owner):
        self.__hidden_owner = owner

    def info(self):  # 멤버 함수
        print(f"{self.owner}의 포켓몬이 사용 가능한 스킬")
        for i in range(len(self.skills)):
            print(f'{i+1} : {self.skills[i]}')
        # for skill in self.skills:  # 번호 붙이고싶을 때 len이나 enmerate?를 쓰는게 좋다 위의 수정본이 적용본
        #     print(f'{skill}')


    def attack(self, idx):
        print(f'{self.skills[idx]} 스킬 시전!')


class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  # 부모 calss 호출할 때 쓰는 것
        self.name = "피카츄"
        print(f"{self.name}")


    def attack(self, idx):  # override
        print(f'[피카피카]{self.owner}의 {self.name}가 {self.skills[idx]} (번개 속성) 스킬 시전!')



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
        print(f'[꼬북꼬북]{self.owner}의 {self.name}가 {self.skills[idx]} (물 속성) 스킬 시전!')


    def swim(self):
        print(f'{self.name}가 수영을 합니다')


class Pairi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  # 부모 calss 호출할 때 쓰는 것
        self.name = "파이리"
        print(f"{self.name}")


    def attack(self, idx):  # override
        print(f'[파일파일]{self.owner}의 {self.name}가 {self.skills[idx]} (북 속성) 스킬 시전!')


while True:
    print(f'총 {Pokemon.count}마리의 포켓몬이 생성되었습니다.')
    menu = input('1) 포켓몬 생성  2) 프로그램 종료 : ')
    if menu == '2':
        print('프로그램을 종료합니다')
        break
    elif menu == '1':
        while True:
            pokemon = input('1) 피카츄 2) 꼬부기 3) 파이리 : ')
            if pokemon == '1':
                n = input('플레이어 이름 입력 : ')
                s = input('사용 가능한 기술 입력(/로 구분하여 입력) : ')
                p = Pikachu(n, s)
                # p.owner = "한지우"  # setter, 허가된 접근
                # p.__hidden_owner = "한지우"  # 허가되지 않은 접근 >> __hidden_owner를 만들어줌으로써 접근이 되지않는것을 확인할 수 있음 / 앞에 클래스를 붙이면 되긴한다
                # 파이썬은 자바와달리 완벽한 프라이빗은 존재하지않는다
                break
            elif pokemon == '2':
                n = input('플레이어 이름 입력 : ')
                s = input('사용 가능한 기술 입력(/로 구분하여 입력) : ')
                p = Ggoboogi(n, s)
                break
            elif pokemon == '3':
                n = input('플레이어 이름 입력 : ')
                s = input('사용 가능한 기술 입력(/로 구분하여 입력) : ')
                p = Pairi(n, s)
                break
            else:
                print('메뉴의 번호를 선택하세요')
        while True:
            info_attack = input('1) 정보 조회  2) 공격 : ')
            if info_attack == '1':
                p.info()
                continue
            elif info_attack == '2':
                p.info()
                attack_menu = input('공격 번호 선택 : ')
                p.attack(int(attack_menu) - 1)
                break
            else:
                print('메뉴의 번호를 선택하세요')
    else:
        print('메뉴의 번호를 선택하세요')



# p0 = Pokemon('웅이', '어떤공격')
# p0.attack(0)
# # p0.swim()  # 꼬부기 클래스의 객체들이 사용할 수 있는 고유 메서드
# pk1 = Pikachu('지우', '전광석화/10만 볼트/전기쇼크/번개')
# # pk1.info()
# ggo1 = Ggoboogi('오박사', '거품/물대포/몸통박치기/껍질에숨기')
# # ggo1.info()
# ggo1.swim()
# pk1.attack(3)
# ggo1.attack(0)
#
# # pi1.info()
# # p1 = Pokemon('웅이', '스핀 테일/브레스/몸통박치기')
# # p2 = Pokemon()