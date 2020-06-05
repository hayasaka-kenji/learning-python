from lesson_package.tools import utils


def sing():
    return 'kjl;jkl;'

def cry():
    return utils.say_twice('jkl;jkl;')

if __name__ == '__main__':
    print(sing())
    print('animal:', __name__)