# クラス
class Person(object):
    def __init__(self, name):
        self.name = name
        print(self.name)

    def say_something(self):
        print(f'I am {self.name}. Hello.')
        # 自身の関数を使う
        self.run(10)

    def run(self, num):
        print('run ' * 10)

person = Person('Mike')
person.say_something()