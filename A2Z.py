# A to Z reminding

# Ch9 practice # 4
class OopsException(Exception):
    pass

while True:
    try:
        things = input('input only q : ')
        if things == 'q':
            raise OopsException('Well done! It\'s q!')
        print('You put wrong thing..')
    except OopsException as err:
        print(err)
    else:
        print("It's okay. Try again.")
    finally:
        print('Keep going!')
