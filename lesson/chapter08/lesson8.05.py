# 書き込み読み込みモード
s = """\
AAA
BBB
CCC
DDD
"""
# w+で書き込み・読み込み
with open('test.txt', 'w+') as f:
    f.write(s)
    # はじめに戻る
    f.seek(0)
    print(f.read())

