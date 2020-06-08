# テンプレート
import string

# 読み込み専用
s = """\
Hi $name.

$contents

Have a good day.
"""

t = string.Template(s)
contents = t.substitute(name='Mike', contents='How are you?')
print(contents)