# list

scores = ('B+', 'A+', 'C+')
print(scores[1], scores[2])
#scores[1] = 'C+'
#scores[2] = 'A+'  # 이렇게 대입하는 것이 안됨 (오류)

temp = list(scores)
temp[1] = 'C+'
temp[2] = 'A+'
scores = tuple(temp)
print(scores[1],scores[2])

a = ['A', 'B', 'C', 'D', 'E']
print(a[0:3])
print(a)
print(a.pop())
print(a)