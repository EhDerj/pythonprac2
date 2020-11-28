from functools import wraps

def deccount(f):
    cntr = 0
    @wraps(f)
    def new(*args, **kwargs):
        nonlocal cntr
        cntr += 1
        print(cntr)
        return f(*args, **kwargs)
    return new