# ファイルの読み込み
with open('test.txt', 'r') as f:
    # print(f.read())
    while True:
        chunk = 2
        line = f.read(chunk)
        # デフォルトが改行ありなので修正
        # print(line, end='')
        print(line)
        if not line:
            break