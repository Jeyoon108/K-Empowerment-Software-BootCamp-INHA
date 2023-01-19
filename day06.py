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


@document_it
def add_ints(a, b):
    return a + b


# # @decorator_name은 def에 직접 사용

add_ints(3, 5)
