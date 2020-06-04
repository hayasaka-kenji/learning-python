# def test_func(x, l = []):
#     l.append(x)
#     return l

# y = [1, 2, 4]
# r = test_func(100, y)
# print(r)
# # [1, 2, 4, 100]
#
# y = [1, 2, 4]
# r = test_func(200, y)
# print(r)
# # [1, 2, 4, 200]

# r = test_func(100)
# print(r)
# # [100]
#
# r = test_func(100)
# print(r)
# # [100, 100]

# Pythonはデフォルト引数でリストを渡すとバグに繋がりやすい。

def test_func(x, l = None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func(100)
print(r)
# [100]

r = test_func(100)
print(r)
# [100]
