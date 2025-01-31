import json
import os

class LibrarySystem:
    def __init__(self, file_name="library_data.json"):
        self.file_name = file_name
        # Load or create the file
        self.books = self.load_books()

    def load_books(self):
        """Load books from JSON file"""
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_books(self):
        """Save books to JSON file"""
        with open(self.file_name, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author, year):
        """Add a new book"""
        new_book = {
            "title": title,
            "author": author,
            "year": year
        }
        self.books.append(new_book)
        self.save_books()
        print(f"Book '{title}' added successfully.")

    def remove_book(self, title):
        """Remove a book by title"""
        self.books = [book for book in self.books if book['title'].lower() != title.lower()]
        self.save_books()
        print(f"Book '{title}' removed successfully.")

    def list_books(self):
        """List all books"""
        if self.books:
            print("Listing all books:")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book['title']} by {book['author']} ({book['year']})")
        else:
            print("No books available.")

    def search_book(self, title):
        """Search for a book by title"""
        found_books = [book for book in self.books if title.lower() in book['title'].lower()]
        if found_books:
            print("Search Results:")
            for book in found_books:
                print(f"{book['title']} by {book['author']} ({book['year']})")
        else:
            print(f"No books found with title '{title}'.")


def main():
    library = LibrarySystem()

    while True:
        print("\nLibrary Management System:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter year of publication: ")
            library.add_book(title, author, year)

        elif choice == '2':
            title = input("Enter book title to remove: ")
            library.remove_book(title)

        elif choice == '3':
            library.list_books()

        elif choice == '4':
            title = input("Enter book title to search for: ")
            library.search_book(title)

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
