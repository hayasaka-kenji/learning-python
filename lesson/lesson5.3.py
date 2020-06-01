y = [1, 2, 4]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

# if not a == b:
#     print('not equal')

# 以下のように書き換えたほうがわかりやすい
if a != b:
    print('not equal')

is_ok = True

# == Trueとしなくていい
if is_ok:
    print('ok')

# 出力されない
if not is_ok:
    print('ok')