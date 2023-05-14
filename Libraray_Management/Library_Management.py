class Library:
 def __init__(self):
   self.noBooks=0
   self.books=[]
   

 def addBook(self, book):
    self.books.append(book)
    self.noBooks = len(self.books)
   

 def showInfo(self):
    print(f"The library has {self.noBooks} books. The books are")
    for book in self.books:
     print(book)

l1 = Library()
l1.addBook("Harry Potter")
l1.addBook("Big Bang")
l1.addBook("Time Machine")
l1.showInfo()
