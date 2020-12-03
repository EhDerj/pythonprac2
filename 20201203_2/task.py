def chan(self):
    for attr, cls in self.__annotations__.items():
        if not (hasattr(self, attr) and isinstance(getattr(self, attr), cls)):
            return False
    return True

class check(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.check_annotations = chan