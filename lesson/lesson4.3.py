num_tuple = 10, 20
print(num_tuple)

# x, y = 10, 20 と同義
x, y = num_tuple
print(x, y)  # 10 20


min, max = 0, 100
print(min, max)  # 0 100
a, b, c, d, e, f = 'hoge', 'fuga', 'piyo', '1', '2', '3'

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

a = 100
b = 200
a, b = b, a
print(a, b)