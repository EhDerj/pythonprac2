from random import randint, choice
vow = 'АЕЁИОУЫЭЮЯ'
con = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ'

N = int(input())
stg = ''
while len(stg) < N:
    if not randint(0,2):
        stg += choice(vow)
    elif randint(0,1):
        stg += choice(vow) + choice(con)
    else:
        stg += choice(con) + choice(vow)
print(stg)