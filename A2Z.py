# A to Z reminding

# Ch10 practice class

class Maple:
    def __init__(self, name, job, skills):
        self.name = name
        self.job = job
        self.skills = skills.split('/')
        print(f'"system" {self.name}이(가) 생성되었습니다.')

    def status(self):
        print(f'당신의 캐릭터 이름은 {self.name}, 직업은 {self.job}입니다.')
        print(f'보유중인 스킬 : {self.skills}')

m1 = Maple('킹왕짱', '아델', '디바이드/블로섬/게더링/다이크')
m1.status()
print()
m2 = Maple('널뛰기공주', '에반', '서클 오브 마나IV/드래곤 브레스/서클 오브 어스/서클 오브 썬더')
m2.status()
