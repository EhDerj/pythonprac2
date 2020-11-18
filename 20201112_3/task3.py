def rnd(fl):
    fl = str(fl.__round__(2))
    if fl[-2] == '.':
        fl += '0'
    return fl

class a(Exception): pass

while c := input():
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(c)
        for i in [x1, x2, x3, y1, y2, y3]:
            if type(i) != int and type(i) != float:
                raise Exception()
        s = abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)) / 2
        if s:
            print(rnd(s))
        else:
            print('Not a triangle')
    except Exception:
        print('Invalid input')
