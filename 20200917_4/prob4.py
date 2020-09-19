a, n = eval(input())

flag = True
x = 0
while (x:=x+1)**n < a and flag:
    y = 0
    while (y := y + 1) ** n < a and flag:
        z = 0
        while (z := z + 1) ** n < a and flag:
            if x**n + y**n + z**n == a:
                print(x, y, z)
                flag = False
if flag:
    print('FAIL')
