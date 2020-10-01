def domen(a, b):
    return a[0] <= b[0] and a[1] <= b[1] and ( a[0] < b[0] or a[1] < b[1] )

def pareto(*a):
    b = list()
    for i in a:
        flag = False
        for j in a:
            flag = domen(i, j)
            if flag: break
        if not flag:
            b.append(i)
    return tuple(b)
