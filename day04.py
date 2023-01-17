# tuple
a = 'harry',
b = ('harry',)
c = ()  # empty tuple
d = 'harry', 'ron'  # packing
e = ('hermione')  # string
f = ('harry', 'ron')  # packing
g = ('hermione',)
print(type(g))
print(f + g)
print(g)
g = f + g
print(g)

print(f[1])
x, y = f  # unpacking
print(x)
print(y)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))