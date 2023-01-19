# # Chap9 # 1
# def good():
#     return ['Harry', 'Ron', 'Hermione']


# Chap9 # 2
count = 0
def get_odds():
    for num in range(10):
        if num % 2 == 1:
            yield num


odds = get_odds()
for i in odds:
    count += 1
    if count == 3:
        print(i)
