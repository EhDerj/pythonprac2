def SUB(a, b):
    if hasattr(a, '__sub__'):
        return a-b
    return type(a)([a[i] for i in range(len(a)) if a[i] not in b])
