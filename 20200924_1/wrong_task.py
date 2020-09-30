a, b = 11, 31
ls = [2i+1 for i in range(a//2, b//2) if '3' not in str(2i+1)]
print(ls)
