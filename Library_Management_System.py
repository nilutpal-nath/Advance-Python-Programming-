class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - [{status}]"


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def __str__(self):
        books = ", ".join([b.title for b in self.borrowed_books]) or "None"
        return f"Patron: {self.name} (ID: {self.patron_id}) | Borrowed: {books}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: '{book.title}'")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f"Registered patron: '{patron.name}'")

    def borrow_book(self, patron_id, isbn):
        patron = next((p for p in self.patrons if p.patron_id == patron_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if not patron or not book:
            print("Error: Patron or Book not found.")
            return
        
        if not book.is_borrowed:
            book.is_borrowed = True
            patron.borrowed_books.append(book)
            print(f"Success: {patron.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently checked out.")

    def return_book(self, patron_id, isbn):
        patron = next((p for p in self.patrons if p.patron_id == patron_id), None)
        
        if not patron:
            print("Error: Patron not found.")
            return

        book = next((b for b in patron.borrowed_books if b.isbn == isbn), None)
        
        if book:
            book.is_borrowed = False
            patron.borrowed_books.remove(book)
            print(f"Success: {patron.name} returned '{book.title}'.")
        else:
            print(f"Error: {patron.name} does not have this book checked out.")

    def display_info(self):
        print(f"\n--- {self.name} Inventory & Status ---")
        print("Books:")
        for book in self.books:
            print(f"  {book}")
            
        print("\nPatrons:")
        for patron in self.patrons:
            print(f"  {patron}")
        print("--------------------------------------\n")


if __name__ == "__main__":
    # 1. Create library instance
    my_lib = Library("Developer Tech Library")

    # 2. Add books (Using the newly provided titles, authors, and ISBNs)
    my_lib.add_book(Book("Python Crash Course", "Eric Matthes", "978-1718502703"))
    my_lib.add_book(Book("Effective Python", "Brett Slatkin", "978-0138172455"))
    my_lib.add_book(Book("The Mythical Man-Month", "Frederick P. Brooks Jr.", "978-0201835953"))
    my_lib.add_book(Book("Clean Code", "Robert C. Martin", "978-0132350884"))

    # 3. Register patrons
    my_lib.register_patron(Patron("Bruce Wayne", "P-001"))
    my_lib.register_patron(Patron("Clark Kent", "P-002"))

    # 4. Display relevant information initially
    my_lib.display_info()

    # 5. Borrow books
    # Bruce borrows 'Python Crash Course'
    my_lib.borrow_book("P-001", "978-1718502703")
    # Clark borrows 'Clean Code'
    my_lib.borrow_book("P-002", "978-0132350884")
    
    # Show updated info after borrowing
    my_lib.display_info()

    # 6. Return books
    # Bruce returns 'Python Crash Course'
    my_lib.return_book("P-001", "978-1718502703")
    
    # Final state display
    my_lib.display_info()