some_list = [1,2,3,4,5]

for i in some_list:
    print(i)

# while文の場合
i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1


for s in 'abcde':
    print(s)

# my
# is
# mike
for w in ['my', 'name', 'is', 'mike']:
    if w == 'name':
        continue
    print(w)