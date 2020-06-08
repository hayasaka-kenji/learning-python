import tempfile

# 一時的にファイルを作る
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# ファイルを残す
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# 一時的にファイルを作る
with tempfile.TemporaryDirectory() as td:
    print(td)

print(tempfile.mkdtemp())