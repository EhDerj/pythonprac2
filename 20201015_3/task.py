from collections import Counter
from random import choices
from sys import argv

choice_dict = lambda d: choices(list(d.keys()), list(d.values()))[0]

N = int(argv[1])

c = Counter()
while a := input().lower():
    c.update([a[i:i+2] for i in range(len(a)-1) if a[i:i+2].isalpha()])

pas = choice_dict(c)
while len(pas) < N:
    pas += choice_dict({i:c[i] for i in c.keys() if i[0] == pas[-1]})[1]

print(pas)