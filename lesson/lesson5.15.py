
# # NameError: name 'say_something' is not defined
# say_something()

# def say_something():
#     print('hi')
#
# # # なにも表示されない
# # say_something
#
# print(type(say_something))
# # <class 'function'>
#
# f = say_something()

def say_something():
    s = 'hi'
    return s

result = say_something()
print(result)

# 引数
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'cabbage'
    else:
        return "I don't know"

# def what_is_this(color):
#     if color == 'red':
#         return 'tomato'
#     if color == 'green':
#         return 'cabbage'
#     return "I don't know"

result = what_is_this('yellow')
print(result)