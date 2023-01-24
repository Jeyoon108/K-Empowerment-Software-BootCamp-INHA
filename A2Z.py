# A to Z reminding

# Ch9 practice # 2

def get_odds():
    for odd in range(10):
        if odd % 2 == 1:
            yield odd


count = 0
for x in get_odds():
    count += 1
    if count == 3:
        print(x)
