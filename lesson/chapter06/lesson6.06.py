# 標準ライブラリ
# 文字の数がいくつあるか確認する

s = 'jkljlkqnflkamcmjr'
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)


d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

from collections import  defaultdict
d = defaultdict(int)
for c in s:
    d[c] += 1
print(d)