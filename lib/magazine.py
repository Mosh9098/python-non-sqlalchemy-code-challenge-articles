class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a string of length 2 to 16 characters.")

    def get_category(self):
        return self._category

    def set_category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string.")
