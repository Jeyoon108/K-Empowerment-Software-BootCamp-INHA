# local, global variable

g = 1
def print_global():
    g = 3
    print(g)


# def change_print_global():
#     print(g)
#     g = 2
#     print(g)  >> error code


def change_print_global():
    global g
    print(g)
    g = 2
    print(g)


print_global()
change_print_global()
print(g)
print(globals())
print(__name__)