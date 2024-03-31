from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.catalog = {}  # Dictionary to store book details by book ID
        self.users = {}    # Dictionary to store user details by user ID

    def display_catalog(self):
        print("Catalog:")
        for book_id, details in self.catalog.items():
            availability = "Available" if details['quantity'] > 0 else "Not Available"
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Availability: {availability}")

    def register_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = {'name': name, 'checked_out_books': {}}
            print(f"User {name} with ID {user_id} registered successfully.")
        else:
            print("User ID already exists. Please choose another ID.")

    def checkout_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not found. Please register first.")
            return
        if book_id not in self.catalog:
            print("Book not found in catalog.")
            return
        if self.catalog[book_id]['quantity'] == 0:
            print("Book not available for checkout.")
            return
        if len(self.users[user_id]['checked_out_books']) >= 3:
            print("Maximum checkout limit reached for this user.")
            return

        self.users[user_id]['checked_out_books'][book_id] = datetime.now()
        self.catalog[book_id]['quantity'] -= 1
        print(f"Book with ID {book_id} checked out successfully by user {self.users[user_id]['name']}.")

    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not found. Please register first.")
            return
        if book_id not in self.users[user_id]['checked_out_books']:
            print("Book not checked out by this user.")
            return

        checkout_date = self.users[user_id]['checked_out_books'].pop(book_id)
        due_date = checkout_date + timedelta(days=14)
        if datetime.now() > due_date:
            overdue_days = (datetime.now() - due_date).days
            fine = overdue_days * 1  # $1 per day overdue
            print(f"Book returned after due date. Overdue fine: ${fine}")
        else:
            print("Book returned successfully.")
        self.catalog[book_id]['quantity'] += 1

    def list_overdue_books(self, user_id):
        if user_id not in self.users:
            print("User not found. Please register first.")
            return
        overdue_books = {}
        total_fine = 0
        for book_id, checkout_date in self.users[user_id]['checked_out_books'].items():
            due_date = checkout_date + timedelta(days=14)
            if datetime.now() > due_date:
                overdue_days = (datetime.now() - due_date).days
                fine = overdue_days * 1  # $1 per day overdue
                total_fine += fine
                overdue_books[book_id] = fine
        if overdue_books:
            print("Overdue Books:")
            for book_id, fine in overdue_books.items():
                print(f"Book ID: {book_id}, Fine: ${fine}")
            print(f"Total Fine Due: ${total_fine}")
        else:
            print("No overdue books for this user.")

# Example usage
library = Library()

# Adding books to catalog
library.catalog = {
    1: {'title': 'Book1', 'author': 'Author1', 'quantity': 3},
    2: {'title': 'Book2', 'author': 'Author2', 'quantity': 2},
    3: {'title': 'Book3', 'author': 'Author3', 'quantity': 1}
}

# Registering users
library.register_user(101, 'User1')
library.register_user(102, 'User2')

# Displaying catalog
library.display_catalog()

# Checkout and return processes
library.checkout_book(101, 1)
library.return_book(101, 1)

# Listing overdue books
library.list_overdue_books(101)