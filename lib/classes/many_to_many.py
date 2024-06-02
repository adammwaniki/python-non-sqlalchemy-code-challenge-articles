class Article:

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value: str):
        if hasattr(self, '_value') and self._title is not None:
            raise AttributeError("Title can only be set once.")
        if isinstance(value, str) and 5<= len(value) <= 50:
            self._title = value
        else:
            raise ValueError("Title must be of type str and between 5 and 50 characters.")
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        if hasattr(self, '_value') and self._name is not None:
            raise AttributeError("Name can only be set once.")
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Title must be of type str and longer than 0 characters.")

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and 2<= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Title must be of type str and longer than 0 characters.")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Title must be of type str and longer than 0 characters.")

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass