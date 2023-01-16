import random

limits = 20
tweets = "pass" * random.randint(1, 10) # 1에서 10사이의 정수가 임의로 발생
diff = limits - len(tweets)
# if diff := limits - len(tweets) >= 0:
if diff >=0:
    print(tweets)
else:
    print(f'제한 글자 수 {abs(diff)}초과')
