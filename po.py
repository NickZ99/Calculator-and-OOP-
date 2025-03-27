class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'"{self.title}" by {self.author}'    

class BookManagementSystem:
    def __init__(self):
        self.books = [] 

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)  
        print(f'Added: {new_book}')

    def view_books(self):
        if not self.books:
            print("No books in the collection.")
        else:
            print("Books in the collection:")
            for book in self.books:
                print(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f'removed:{book}')
                return
        print(f'Book titled "{title}" not found in the collection.')

    def run(self):
        while True:
            print("\nBook Management System")
            print("1. Add Book")
            print("2. View Books")
            print("3. Remove Book")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                year = input("Enter the year of the book: ")
                self.add_book(title, author, year)
            elif choice == '2':
                self.view_books()
            elif choice == '3':
                title = input("Enter the title of the book to remove: ")
                self.remove_book(title)
            elif choice == '4':
                print("Exiting the system, goodbye!")
                break
            else:
                print("Invalid choice, Please try again")

if __name__ == "__main__":
    system = BookManagementSystem()
    system.run()