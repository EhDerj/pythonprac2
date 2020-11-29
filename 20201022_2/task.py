from itertools import tee, islice

def even(seq):
    yield from filter(lambda x: not x%2, seq)

def slide(seq):
    seq = iter(seq)
    while True:
        seq, tmp = tee(seq, 2)
        if len(a := list(islice(tmp, 3))) == 3:
            yield from even(a)
            next(seq)
        else:
            return