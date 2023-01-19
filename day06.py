# generator 예제

# decorator
def document_it(func):
    def new_function(*args,**kwargs):
        print('Running function:', func.__name__)  # 실행중인 함수
        print('Positional arguments:', args)  # 위치 기반 인수들
        print('Keyword arguments:', kwargs)  # 키워드 기반 인수들
        result = func(*args, **kwargs)
        print('Result:', result)  # 실행 결과
        return result
    return new_function


def add_ints(a, b):
    return a + b


# manual decorator assignment (데커레이터 수동 할당)

print(add_ints(3, 5))
info_add_ints = document_it(add_ints)
info_add_ints(3, 5)
