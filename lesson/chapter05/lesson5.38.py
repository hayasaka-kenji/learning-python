# 名前空間
def f():
    """Test func doc"""
    print(f.__name__)
    print(f.__doc__)

f()
print('global:', globals())
