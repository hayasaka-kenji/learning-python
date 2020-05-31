r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3)) # 2
print(r.index(3, 3)) # 7

print(r.count(3)) # 2

print(5 in r) # True

print('-----------')

r.sort()
print(r) # [1, 1, 2, 2, 3, 3, 4, 5]

r.sort(reverse=True)
print(r) # [5, 4, 3, 3, 2, 2, 1, 1]

r.reverse()
print(r)

print('-----------')

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split) # ['My', 'name', 'is', 'Mike']
x = ' '.join(to_split)
print(x) # My name is Mike

help(list)