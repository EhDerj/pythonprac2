s = input()

# let's say string starts numerating from 1, not from 0
# (it's just looks nicer and this kind of counting more familiar)
flag, last = False, ''
for i, elem in enumerate(s):
    if elem in {'1','2','3','4','5'}:
        last = elem
        continue
    if flag:
        print(i, last)
    if elem == 'B': flag = True
    else: flag = False
if flag:
    print(len(s), last)