# A to Z reminding

# Ch9 practice # 3

def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print(result)
        print('end')
        return result

    return new_func

# @test >> 데커레이터 수동 할당 대안
def subs_ints(a, b):
    return a - b


new_subs_ints = test(subs_ints)  # 데커레이터 수동 할당

print(subs_ints(5, 3))
new_subs_ints(5, 3)  # 수동 할당 결과
