print("I'm a boy")

# army = '''우리는 국가와 국민에 충성을 다하는 대한민국 육군이다.
# 하나 우리는 자유민주주의를 수호하며 조국 통일의 역군이 된다.'''
army = '우리는 국가와 국민에 충성을 다하는 대한민국 육군이다.\t하나 우리는 자유 민주주의 어쩌구'

print(army)

start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'

print(start + start + middle + end)

name = 'Call'
print(name[0])
print('B'+name[1:])
print(name[::2])

univ = 'Inha University'
print(univ.split('i'))

pokemons_list = ['봉준호', '손흥민', 'Black Pink', 'Jay Park']
pokemons_string = ', '.join(pokemons_list) + " let's go"
print(pokemons_string)

test = ['a', 'b', 'c']
test[0] = 'd'
print(test)

print(univ.replace('Inha', 'King god Inha'))

subjects = '  ! $   python, data structure, database @   !'
print(subjects.strip(' !'))

subjects = '  ! $   python, data structure, database @   !'
print(subjects.find('data'), subjects.index('data'))
print(subjects.find('inha')) # return -1
#print(subjects.index('inha')) # Exception
print(subjects.count('data'))

letters_1 = 'I got your back, buddy'
letters_2 = 'Igotyourback123 '
print(letters_2.isalnum())
print(letters_2.strip(' ').isalnum())