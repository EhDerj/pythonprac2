l = list()
while s:= input():
    l.append(s)

prev = set()
for i, s in enumerate(l):
    post = set()
    for j in range(i+1, len(l)):
        post |= set(l[j])
    if not (set(s) & (prev | post)):
        print(s)
    prev |= set(s)