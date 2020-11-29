def find_max_wide(n, lg):
    k = 1
    while True:
        res = 9 * k - 3
        for i in range(1, k + 1):
            m = (n-1) // k
            if m * k + i > n:
                m -= 1
            res += len(str(m * k + i)) + len(str(n)) + len(str((m * k + i) * n))
        if res > lg:
            k -= 1
            break
        k += 1
    ls = list()
    for i in range(1, k + 1):
        m = (n - 1) // k
        if m * k + i > n:
            m -= 1
        ls.append([len(str(m * k + i)), len(str(n)), len(str((m * k + i) * n))])
    return k, ls

def print_table(n, lg):
    wd, ls = find_max_wide(n, lg)
    if not wd: return
    print('=' * lg)
    for l in range(n//wd + int(bool(n%wd))):
        for j in range(1, n + 1):
            st = '{m1:>{ln[0]}} * {m2:<{ln[1]}} = {pr:<{ln[2]}}'.format(
                m1= l*wd + 1, m2= j, pr= (l*wd + 1) * j, ln= ls[0]
            )
            for i in range(l*wd + 2, min(n, (l+1)*wd) + 1):
                st += ' | {m1:>{ln[0]}} * {m2:<{ln[1]}} = {pr:<{ln[2]}}'.format(
                    m1=i, m2=j, pr=i * j, ln=ls[i%wd-1]
                )
            print(st)
        print('=' * lg)

while s := input():
    print_table(*eval(s))