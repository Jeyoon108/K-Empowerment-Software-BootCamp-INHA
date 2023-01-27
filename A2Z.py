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

m0 = Maple('초보자')
m0.status()
print()
m1 = Adele('킹왕짱')
m1.status()
m1.skill(2)
m1.skill(1)
print()
m2 = Evan('도끼차')
m2.status()
m2.skill(0)
