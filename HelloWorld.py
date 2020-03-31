import math
import sys
from os import rename

import requests


print(sys.version)
print(sys.executable)


def greet(who_to_great):
    greeting = "Hello, {}".format(who_to_great)
    return greeting


print(greet("World"))
print(greet("Boris"))
r = requests.get("https://elysee.fr")
print(r.status_code)
name = input('what is your name ?')
# print("Hello, {}".format(name))
# print('Hello', name)
