class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self.__title = title

    @property
    def title(self):
        return self.__title
