print('P', 'T', 'A', sep=',', end='.\n')

import math
x = math.sqrt(25)
print(x) # 5.0 (平方根)

y = math.log2(10)
print(y) # 3.321928094887362 （ログ）

print(help(math)) # ヘルプ関数の表示

print('Hello \nHow are you')

print(r'C:\dir\file') # C:\dir\file

print("""
line1
line2
line3
""")

print('#######')
print("""\
line1
line2
line3\
""")
print('#######')

print('Hi.' * 3 + 'Mike')

word = 'python'
print(word[0]) # p
print(word[-1]) # n
print(word[1:3]) # yt
print(word[:3]) # pyt # 最初から3文字目まで
print(word[2:]) # thon # 2文字目から最後まで
print(word[:]) # 最初から最後まで
n = len(word)
print(n)
word = 'j' + word[1:]
print(word) # jython

s = 'My name is Mike. Hi Mike.'

# 最初の文字列を確認する
is_start = s.startswith('My')
print(is_start) # True
is_start = s.startswith('X')
print(is_start) # False

# 文字列を探す。rfindは最後から探す。
print(s.find('Mike'))
print(s.rfind('Mike'))
# 何度でてきたか測定する。
print(s.count('Mike'))
# 最初は大文字ほかは小文字
print(s.capitalize()) # My name is mike. hi mike.
# 単語の頭文字を大文字に
print(s.title()) # My Name Is Mike. Hi Mike.
# 指定した文字列を変換する
print(s.replace('Mike', 'Nancy')) # My name is Nancy. Hi Nancy.