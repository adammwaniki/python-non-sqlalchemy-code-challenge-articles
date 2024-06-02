class Article:
    
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value: str):
        # Inserting an extra condition to handle fringe cases like the someone declaring the title as None
        if hasattr(self, '_title') and self._title is not None:
            raise AttributeError("Title can only be set once.")
        if isinstance(value, str) and 5<= len(value) <= 50:
            self._title = value
        else:
            raise ValueError("Title must be of type str and between 5 and 50 characters.")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self,value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError("Must be of type Author")   
        
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self,value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise ValueError("Must be of type Magazine")   
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        # Inserting the same extra condition as in the Article for handling None
        if hasattr(self, '_name') and self._name is not None:
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
            raise ValueError("Magazine name must be of type str and longer than 0 characters.")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be of type str and longer than 0 characters.")

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass