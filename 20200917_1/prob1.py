a = int(input())

if a%25 :
    print('A-\nB- ')
elif a%2 :
    print('A-\nB+ ')
else:
    print('A+\nB- ')

if a%8 :
    print('C-')
else:
    print('C+')
