def say_something(word, *args):
    print('word = ', word)
    for arg in args:
        print(arg)

say_something('Hello', 'Mike', 'Nance')

t = ('Mike', 'Nance')
say_something('Hello', *t)