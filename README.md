# Library Management System

This is a **Library Management System** built using Python and the Tkinter library for the graphical user interface. It allows users to manage a library's collection of books, including adding, updating, borrowing, and returning books. The application uses an SQLite database to store all book records.

---

## Features

- **Add New Books:** Add books with details like Title, Author, and Genre.
- **View All Books:** Display the list of all books in the library.
- **Update Book Information:** Edit book details like Title, Author, or Genre.
- **Delete Books:** Remove books from the database.
- **Search Books:** Search for books by Title or Author.
- **Filter Books:** Filter books by Genre.
- **Borrow and Return Books:** Mark books as borrowed or returned.
- **View Borrowed Books:** Display a list of books currently borrowed.
- **Book Count Display:** Shows the total number of books and the number of borrowed books.

---

## Installation

Follow these steps to set up the Library Management System:



1. **Install Python:**
   Ensure that Python 3.8 or higher is installed on your system.

   - Check Python version:
     ```bash
     python --version
     ```

2. **Install Required Libraries:**
   The program uses Tkinter (comes pre-installed with Python) and SQLite3 (built-in with Python).
   No additional libraries are needed.

---

## How to Run

1. Open a terminal or command prompt in the project directory.
2. Run the program by executing the following command:
   ```bash
   python library_management_system.py
   ```
3. The graphical interface will launch, and you can start managing the library.

---

## Program Usage

### Adding a New Book

1. Enter the book's **Title**, **Author**, and **Genre** in the input fields.

2. Click the **Add Book** button to save the book to the database.

### Viewing All Books

- Click the **View Books** button to display all books in the library.

### Searching for Books

1. Type the search term (Title or Author) in the **Search Books** field.
2. Click the **Search** button to find matching books.
3. To clear the search, click the **Clear Search** button.

### Filtering by Genre

1. Use the **Filter by Genre** dropdown menu to display books based on their genre.

### Updating a Book

1. Select a book from the table by clicking on it.
2. Edit the **Title**, **Author**, or **Genre** fields.
3. Click the **Update Book** button to save changes.

### Deleting a Book

1. Select a book from the table by clicking on it.
2. Click the **Delete Book** button to remove the book from the library.

### Borrowing and Returning Books

1. Select a book from the table.
2. Click **Borrow** to mark the book as borrowed (only if the book is available).
3. Click **Return** to mark the book as available again.

### Viewing Borrowed Books

- Click the **View Borrowed** button to display books that have been borrowed.

### Viewing Book Details

- Select a book and click **View Book Details** to see detailed information about the book.

### Book Counts

- The **Total Books** and **Borrowed Books** counts are displayed above the table and update automatically.

---

## Dependencies

- Python 3.8 or higher
- Tkinter (built into Python)
- SQLite3 (built into Python)

---

## Screenshots

1. **Main Window:**
![alt text](<Screenshot 2024-12-17 145730.png>)
2. **Add Book Form:**
![alt text](<Screenshot 2024-12-17 143758.png>)
3. **Book Table:**
   Displays book details like ID, Title, Author, Genre, and Availability.
![alt text](<Screenshot 2024-12-17 145406.png>)
4. **Borrow/Return Books:**
![alt text](<Screenshot 2024-12-17 150005.png>)
---

## Notes

- The program creates an SQLite database file named `booklibrary.db` automatically.
- The database and records persist across program runs.
- All book data is indexed for faster searching.

---

Happy Reading! 📚

