# A to Z reminding

# Ch10 practice class

class Maple:
    def __init__(self, name):
        self.name = name
        print(f'"system" {self.name}이(가) 생성되었습니다.')


    def status(self):
        print(f'당신의 캐릭터 이름은 {self.name}, 전직이 필요합니다.')
        print(f'보유중인 스킬 : 없음')

class Adele(Maple):
    def __init__(self, name):
        super().__init__(name)
        self.job = "아델"
        self.skills = ['디바이드', '블로섬', '게더링', '다이크']


    def status(self):
        print(f'당신의 캐릭터 이름은 {self.name}, 직업은 {self.job}입니다.')
        print(f'보유중인 스킬 : {self.skills}')


    def skill(self,idx):
        print(f'{self.name}의 {self.skills[idx]}스킬 사용!')

class Evan(Maple):
    def __init__(self, name):
        super().__init__(name)
        self.job = "에반"
        self.skills = ['서클 오브 마나IV', '드래곤 브레스', '서클 오브 어스', '서클 오브 썬더']


    def status(self):
        print(f'당신의 캐릭터 이름은 {self.name}, 직업은 {self.job}입니다.')
        print(f'보유중인 스킬 : {self.skills}')


    def skill(self,idx):
        print(f'{self.name}의 {self.skills[idx]}스킬 사용!')

while True:
    menu = input('1) 캐릭터 생성  2) 프로그램 종료 : ')
    if menu == '2':
        print('프로그램을 종료합니다')
        break
    elif menu == '1':
        while True:
            job = input('1) 아델 2) 에반 3) 초보자 : ')
            if job == '1':
                n = input('플레이어 이름 입력 : ')
                p = Adele(n)
                break
            elif job == '2':
                n = input('플레이어 이름 입력 : ')
                p = Evan(n)
                break
            elif job == '2':
                n = input('플레이어 이름 입력 : ')
                p = Maple(n)
                break
            else:
                print('메뉴의 번호를 선택하세요')
        while True:
            info_skill = input('1) 정보 조회  2) 스킬사용 : ')
            if info_skill == '1':
                p.status()
                continue
            elif info_skill == '2':
                p.status()
                attack_menu = input('공격 번호 선택 : ')
                p.skill(int(attack_menu) - 1)
                break
            else:
                print('메뉴의 번호를 선택하세요')
    else:
        print('메뉴의 번호를 선택하세요')

# m0 = Maple('초보자')
# m0.status()
# print()
# m1 = Adele('킹왕짱')
# m1.status()
# m1.skill(2)
# m1.skill(1)
# print()
# m2 = Evan('도끼차')
# m2.status()
# m2.skill(0)
