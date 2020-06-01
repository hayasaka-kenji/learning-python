# 集合の使い所
my_friends = {'A', 'B', 'C'}
your_friends = {'B', 'D'}

# 共通は 'B'と表示される
print(my_friends & your_friends)


cart = ['apple', 'banana', 'apple', 'banana']
kind = set(cart)

# 共通は'apple', 'banana'と表示される。
print(kind)