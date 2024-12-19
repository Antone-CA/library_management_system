from library_system import LibraryManagementSystem


def main():
    import tkinter as tk
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()


if __name__ == "__main__":
    main()
