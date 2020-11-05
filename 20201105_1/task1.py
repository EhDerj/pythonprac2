from re import match
print(bool(match(r'[+-]?(\d+|\d*\.\d+|\d+\.\d*)([eE][+-]?\d+)?$', input())))
