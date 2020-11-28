class Num:
    def __get__(self, obj, cls):
        if hasattr(obj, "_value"):
            return obj._value
        else:
            return 0

    def __set__(self, obj, val):
        if hasattr(val, "__len__"):
            obj._value = len(val)
        else:
            obj._value = val

    def __delete__(self, obj):
        obj._value = None