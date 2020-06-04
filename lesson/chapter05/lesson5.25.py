# クロージャ
def outer(a, b):

    def inner():
        return a + b

    # ファンクションのオブジェクトにしておく
    return inner

# print(outer(1, 2))

f = outer(1, 2)

print('####')

r = f()
print(r)