# 内包表記

t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9)


r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)

# 取り出してそのままつかえる。条件式もそのままかける
# メモリ消費が少ない。
r = [i for i in t if i % 2 == 0 ]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)

# 追加されるものを最初に書いている。
r = [i * j for i in t for j in t2]
print(r)

# 使えるから使うではなく、読みやすいかどうかで判断するようにする。
