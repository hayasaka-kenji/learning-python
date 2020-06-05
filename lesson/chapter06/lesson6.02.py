# 1
import lesson_package.tools.utils
r = lesson_package.tools.utils.say_twice('hello')

# 2
from lesson_package.tools import utils

r = utils.say_twice('hello')

# 3
from lesson_package.tools.utils import say_twice
r = say_twice('hello')

print(r)