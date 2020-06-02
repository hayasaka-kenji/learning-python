# 引数と返り値の型を指定する
def add_num(a:int, b:int) -> int:
    return a + b

print(add_num(10, 20))
# 30

print(add_num('a', 'b'))
# ab エラーとして返ってこない。
