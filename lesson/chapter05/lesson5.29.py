# デコレーター
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

# 順番を返ると違う結果が返ってくる。
@print_info
@print_more
def add_num(a, b):
    return a + b

a = add_num(10, 20)
print(a)