i = [1, 2, 3, 4, 5]
j = i
j[0] = 100

print('i => ', i)
print('j => ', j) # 参照渡しが発生

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('x => ', x)
print('y => ', y)

print('i id => ', id(i)) # 同じ
print('j id => ', id(j)) # 同じ
print('x id => ', id(x)) # 異なる
print('y id => ', id(y)) # 異なる