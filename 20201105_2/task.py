from re import search, sub
a = input()
if search('[aeiouy].+[aeiouy]', a):
    a = sub(r'([^aeiouy]+)([aeiouy])([^aeiouy]+)([aeiouy])(.+)', r'\1\4\3\2\5', a)
print(a)