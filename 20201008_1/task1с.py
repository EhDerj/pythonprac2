mesh = [80, 25]
seg_x = [-5, 5]
seg_y = [-3, 3]

def cell_2_point(x):
    return seg_x[0] + (x + 0.5) * (seg_x[1] - seg_x[0]) / mesh[0]

def point_2_cell(y):
    return int((y - seg_y[0]) * mesh[1] / (seg_y[1] - seg_y[0]))

def new_line(n):
    s = '{: >{}}'.format('*', n[0])
    for i in range(1, len(n)):
        s += '{: >{}}'.format('*', n[i]-n[i-1])
    return '{: <{}}'.format(s, mesh[0])

def mesh_ver(f):
    ls = list()
    for x in range(mesh[0]):
        y = point_2_cell(f(cell_2_point(x)))
        for i in ls:
            if i[0] == y:
                i.append(x)
                break
        else:
            if 0 < y < mesh[1]: ls.append([y, x])
    ls.sort(key=lambda a: a[0], reverse=True)
    j = 0
    for i in reversed(range(mesh[1])):
        if j < len(ls) and i == ls[j][0]:
            print(new_line(ls[j][1:]))
            j += 1
        else:
            print(' ' * mesh[0])


from math import *

s = input()
if sg := input():
    seg_x, seg_y = list(eval(sg)[:2]), list(eval(sg)[2:])
mesh_ver(lambda x: eval(s))