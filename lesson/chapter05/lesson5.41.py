# 独自例外

# raise IndexError('test error')

class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)
try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')
# Traceback (most recent call last):
#   File "learning-python/lesson/lesson5.41.py", line 14, in <module>
#     check()
#   File "learning-python/lesson/lesson5.41.py", line 12, in check
#     raise UppercaseError(word)
# __main__.UppercaseError: APPLE