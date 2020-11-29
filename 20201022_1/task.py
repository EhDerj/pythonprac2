def fib(m, n):
    if m == 1: yield 1
    last, k = [0, 1], 1
    while (k:=k+1) <= n:
        last.append(last[0] + last[1])
        last.pop(0)
        if k >= m: yield last[1]
