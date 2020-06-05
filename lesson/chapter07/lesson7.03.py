# コンストラクタとデストラクタ
class Person(object):
    # コンストラクタ
    def __init__(self, name):
        self.name = name
        print(self.name)

    def say_something(self):
        print(f'I am {self.name}. Hello.')
        # 自身の関数を使う
        self.run(10)

    def run(self, num):
        print('run ' * 10)

    # デストラクタ
    def __del__(self):
        print('good bye')

person = Person('Mike')
person.say_something()
# del person

print('---------')