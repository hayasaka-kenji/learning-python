# seek
with open('test.txt', 'r') as f:
    f.seek(4)
    print(f.read(1))