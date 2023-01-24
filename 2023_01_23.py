# A to Z reminding

# Ch7 practice # 10

even_numbs = [num for num in range(10) if num % 2 == 0]
print(even_numbs)

# Ch7 practice # 11

# rhymes의 각 튜플 첫 번째, 두 번째에서,
# start1의 첫 글자를 대문자로 만들고 각 단어 뒤에 느낌표와 공백 출력
# 이어서 rhymes의 첫 번째 문자열 대문자, 느낌표 출력
# 두 번째는 start2와 공백 출력 후 두 번째 문자열과 마침표를 출력
# ex) Fee! Fie! Foe! Flop!
#     Someone better get a mop.
#     ...

start1 = ["fee", "fie", "foe"]
rhymes = [("flop", "get a mop"),
          ("fope", "turn the rope"),
          ("fa", "get your ma"),
          ("fudge", "call the judge"),
          ("fat", "pet the cat"),
          ("fog", "walk the dog"),
          ("fun", "say we're done"),
          ]
start2 = "Someone better"

for idx in range(0, len(start1)):
    start1[idx] = start1[idx].capitalize()

for k, j in rhymes:
    for i in range(0, len(start1)):
        print(f"{start1[i].capitalize()}!", end=' ')
    print(f'{k.capitalize()}!')
    print(f'{start2} {j}.')
