# practice Ch9

def start_end(func):
    def new_function():
        print('start')
        result = func()
        print('end')
        return result

    return new_function

def nothing():
    print('nothing')
    return nothing

start_nothing = start_end(nothing())


