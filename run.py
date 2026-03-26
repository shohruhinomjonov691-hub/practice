# Dunder _builtins_, _init_
message = "PYTHON: Everything is object!"
print(message)

result = type(message)
print("result:", result)

''' In Python, there are builtin tools:
(1) TYPES > int float str list dict
(3) FUNCTIONS > print() len() input() type() str() int()
(4) CONSTANTS > True False None
'''

print(dir(__builtins__))