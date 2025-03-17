#source: https://www.geeksforgeeks.org/python-__repr__-magic-method/
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
 
    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"
 
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
 
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224)
 
print("Using str(): ", str(book1))
print("Using repr(): ", repr(book1))