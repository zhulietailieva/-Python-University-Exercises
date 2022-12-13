class Book:
    def __init__(self,book_name,book_code,book_price,book_year,book_author):
        self.book_name=book_name
        self.book_code=book_code
        self.book_price=book_price
        self.book_year=book_year
        self.book_author=book_author

    def book_info(self):
        return f'{self.book_name} - {self.book_code} - {self.book_price}$ - {self.book_year} - {self.book_author}'


book1=Book('Harry Potter',100,20,2001,'J. K. Rowling')
book2=Book('Alice in Wonderland',101,15,1921,'Lewis Carrol')
book3=Book('Discovery of India',102,10,2016,'Jawaharlal Nehru')
book4=Book('Old Man and the Sea',103,50,1997,'Ernest Hemingway')
book5=Book('Fantastic Beasts and Where to Find Them:',104,45,2015,'J. K. Rowling')

books=[book1,book2,book3,book4,book5]


def sort_name(items):
    sorted_items=sorted(items,key=lambda book:book.book_name, reverse=True)
    for book in sorted_items:
        print(book.book_info())


def author(author_name,items):
    result=[]
    for item in items:
        if(item.book_author==author_name):
            result.append(item)
    for book in result:
        print(book.book_info())


def search(book_code,items):
    for item in items:
        if(item.book_code==book_code):
            print(item.book_year)
            return
    print('The book is not found')


print('Sorted books by name descending:')
sort_name(books)
print()

print('Books by J. K. Rowling: ')
author('J. K. Rowling',books)
print()

print('book_code test:')
search(103,books)





