from re import search, sub
from sys import exit
a = input()
if not search('[aeiouy].+[aeiouy]', a):
    exit()
print(sub(r'([^aeiouy]+)([aeiouy])([^aeiouy]+)([aeiouy])(.+)', r'\1\4\3\2\5', a))