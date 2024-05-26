class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            raise ValueError("Name must be a non-empty string.")
    
    @property
    def name(self):
        return self.__name
