# 書き込み読み込みモード
s = """\
AAA
BBB
CCC
DDD
"""
# r+で読み込み・書き込み（ファイルがないとエラーになる。）
with open('test.txt', 'r+') as f:
    print(f.read())