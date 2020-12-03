from types import FunctionType

def dec(f):
    def new(self, *args, **kwargs):
        print(f"{f.__name__}: {args}, {kwargs}")
        return f(self, *args, **kwargs)
    return new

class dump(type):
    def __init__(cls, *args, **kwargs):
        for attr, obj in vars(cls).items():
            if isinstance(obj, FunctionType):
                setattr(cls, attr, dec(obj))
        super().__init__(*args, **kwargs)