# テンプレート
import string

# 読み込み専用
with open('../../design/template.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Mike', contents='How are you?')
print(contents)