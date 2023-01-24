# A to Z reminding

# Ch8 practice # 1 ~ # 5

e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}

print(e2f['walrus'])

f2e = {values: keys for keys, values in e2f.items()}
print(f2e)

print(f2e['chien'])

print(list(e2f.keys()))
