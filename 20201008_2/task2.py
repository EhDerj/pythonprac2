from fractions import Fraction as frac

def str2rl(st):
    st = st.split(', ')
    for i in range(len(st)):
        st[i] = float(frac(st[i]))
    return st

def str2fc(st):
    st = st.split(', ')
    for i in range(len(st)):
        st[i] = frac(st[i])
    return st

def polynomizer(n, ls):
    l = list()
    for i in range(int(n) + 1):
        l.append(ls.pop(0))
    def f(x):
        res = 0
        for i in range(int(n) + 1):
            res += l[i] * x ** (n - i)
        return res
    return f

def polynom_check(main):
    s, w = main.pop(0), main.pop(0)
    A, B = polynomizer(main.pop(0), main), polynomizer(main.pop(0), main)
    if B(s) == 0: return False
    return A(s) / B(s) == w