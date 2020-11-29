import sys

name, pnum = sys.argv[1], int(sys.argv[2])

with open(name, "rb") as f:
    data = f.read()

sz = len(data) // pnum
t = (data[i*sz:(i+1)*sz+1] for i in range())


with open(name, "wb") as f:
    for i in range(pnum):
        f.write(data[])