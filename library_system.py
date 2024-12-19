import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3


class LibrarySystemDatabase:
    def __init__(self):
        self.db_name = 'booklibrary.db'
        self.create_db()

    def create_db(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            genre TEXT,
            avail INTEGER DEFAULT 1
        )""")
        conn.commit()
        conn.close()

    def connect_db(self):
        return sqlite3.connect(self.db_name)

    def fetch_all_books(self):
        conn = self.connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()
        conn.close()
        return rows

    def insert_book(self, title, author, genre):
        conn = self.connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)", (title, author, genre))
        conn.commit()
        conn.close()

    def update_book_in_db(self, book_id, title, author, genre):
        conn = self.connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE books SET title=?, author=?, genre=? WHERE id=?", (title, author, genre, book_id))
        conn.commit()
        conn.close()

    def delete_book_from_db(self, book_id):
        conn = self.connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE id=?", (book_id,))
        conn.commit()
        conn.close()

    def borrow_book_in_db(self, book_id):
        conn = self.connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE books SET avail = 0 WHERE id=?", (book_id,))
        conn.commit()
        conn.close()

    def return_book_in_db(self, book_id):
        conn = self.connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE books SET avail = 1 WHERE id=?", (book_id,))
        conn.commit()
        conn.close()

    def search_books_in_db(self, search_term):
        conn = self.connect_db()
        cur = conn.cursor()
        query = "SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR genre LIKE ?"
        cur.execute(query, ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
        rows = cur.fetchall()
        conn.close()
        return rows


class LibraryManagementSystem(LibrarySystemDatabase):
    def __init__(self, root):
        super().__init__()

        self.root = root
        self.root.title("Library Management System")
        self.root.configure(bg='#736F6E')
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="BOOK E-LIBRARY", font=("Arial", 30, "bold"), bg='#98918F', fg="white")
        self.title_label.pack(pady=10)

        self.details_frame = tk.Frame(self.root, bg='#98918F')
        self.details_frame.pack(pady=10)

        tk.Label(self.details_frame, text="Title:", font=("Arial", 10, "bold"), bg='#98918F', fg='white').grid(row=0, column=0, padx=10, pady=5)
        self.title_entry = tk.Entry(self.details_frame)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.details_frame, text="Author:", font=("Arial", 10, "bold"), bg='#98918F', fg='white').grid(row=1, column=0, padx=10, pady=5)
        self.author_entry = tk.Entry(self.details_frame)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.details_frame, text="Genre:", font=("Arial", 10, "bold"), bg='#98918F', fg='white').grid(row=2, column=0, padx=10, pady=5)
        self.genre_entry = tk.Entry(self.details_frame)
        self.genre_entry.grid(row=2, column=1, padx=10, pady=5)

        self.button_frame = tk.Frame(self.root, bg='#98918F')
        self.button_frame.pack(pady=10)

        tk.Button(self.button_frame, text="Add Book", font=("Arial", 10, "bold"), bg='#98918F', fg='white', command=self.add_book).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(self.button_frame, text="Update Book", font=("Arial", 10, "bold"), bg='#98918F', fg='white', command=self.update_book).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.button_frame, text="Delete Book", font=("Arial", 10, "bold"), bg='#98918F', fg='white', command=self.delete_book).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(self.button_frame, text="Borrow Book", font=("Arial", 10, "bold"), bg='#98918F', fg='white', command=self.borrow_book).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(self.button_frame, text="Return Book", font=("Arial", 10, "bold"), bg='#98918F', fg='white', command=self.return_book).grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.button_frame, text="Search", font=("Arial", 10, "bold"), bg='#98918F', fg='white', command=self.search_books).grid(row=1, column=2, padx=10, pady=5)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Title", "Author", "Genre", "Availability"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Genre", text="Genre")
        self.tree.heading("Availability", text="Availability")
        self.tree.pack(pady=10)

        self.view_books()

    def view_books(self):
        rows = self.fetch_all_books()
        self.clear_tree()
        for row in rows:
            row = list(row)
            row[4] = "Available" if row[4] == 1 else "Borrowed"
            self.tree.insert("", "end", values=row)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        if title and author and genre:
            self.insert_book(title, author, genre)
            messagebox.showinfo("Success", "Book added successfully!")
            self.view_books()

    def update_book(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Select a book to update.")
            return
        values = self.tree.item(selected, "values")
        if values:
            book_id = values[0]
            title = self.title_entry.get()
            author = self.author_entry.get()
            genre = self.genre_entry.get()
            self.update_book_in_db(book_id, title, author, genre)
            messagebox.showinfo("Success", "Book updated successfully!")
            self.view_books()

    def delete_book(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Select a book to delete.")
            return
        values = self.tree.item(selected, "values")
        if values:
            book_id = values[0]
            self.delete_book_from_db(book_id)
            messagebox.showinfo("Success", "Book deleted successfully!")
            self.view_books()

    def borrow_book(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Select a book to borrow.")
            return
        values = self.tree.item(selected, "values")
        if values:
            book_id = values[0]
            if values[4] == "Available":
                self.borrow_book_in_db(book_id)
                messagebox.showinfo("Success", "Book borrowed successfully!")
                self.view_books()
            else:
                messagebox.showerror("Error", "Book is already borrowed.")

    def return_book(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "Select a book to return.")
            return
        values = self.tree.item(selected, "values")
        if values:
            book_id = values[0]
            if values[4] == "Borrowed":
                self.return_book_in_db(book_id)
                messagebox.showinfo("Success", "Book returned successfully!")
                self.view_books()
            else:
                messagebox.showerror("Error", "Book is already available.")

    def search_books(self):
        search_term = self.title_entry.get()
        if not search_term:
            messagebox.showerror("Error", "Enter a search term.")
            return
        rows = self.search_books_in_db(search_term)
        self.clear_tree()
        for row in rows:
            row = list(row)
            row[4] = "Available" if row[4] == 1 else "Borrowed"
            self.tree.insert("", "end", values=row)

    def clear_tree(self):
        self.tree.delete(*self.tree.get_children())


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()