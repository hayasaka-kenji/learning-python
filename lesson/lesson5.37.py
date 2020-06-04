# 名前空間
animal = 'cat'

def f():
    # エラー
    print(animal)
    animal = 'dog'
    # こっちはうまくいく
    print(animal)

f()