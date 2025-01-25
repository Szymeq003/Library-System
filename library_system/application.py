import tkinter as tk
from tkinter import messagebox
from .library import Biblioteka
from .add_book_window import AddBookWindow
from .search_book_window import SearchBookWindow

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.configure(bg="#e0f7fa")  # Light cyan background
        self.pack(fill=tk.BOTH, expand=True)
        self.biblioteka = Biblioteka()
        self.create_widgets()

    def create_widgets(self):
        # Main frame to center content
        self.main_frame = tk.Frame(self, bg="#e0f7fa")
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Title label
        self.titleLabel = tk.Label(self.main_frame, text="System Biblioteczny", font=("Helvetica", 24, "bold"), bg="#e0f7fa")
        self.titleLabel.pack(pady=20)

        # Frame for buttons
        self.button_frame = tk.Frame(self.main_frame, bg="#e0f7fa")
        self.button_frame.pack(pady=10)

        self.addButton = tk.Button(self.button_frame, text="Dodaj książkę", command=self.add_book, width=20, height=2, bg="#4caf50", fg="white", font=("Helvetica", 14, "bold"), bd=2, relief="solid", highlightthickness=3, highlightbackground="#388e3c", highlightcolor="#388e3c")
        self.addButton.grid(row=0, column=0, padx=10, pady=10)

        self.viewButton = tk.Button(self.button_frame, text="Wyświetl wszystkie książki", command=self.view_books, width=20, height=2, bg="#2196f3", fg="white", font=("Helvetica", 14, "bold"), bd=2, relief="solid", highlightthickness=3, highlightbackground="#1976d2", highlightcolor="#1976d2")
        self.viewButton.grid(row=0, column=1, padx=10, pady=10)

        self.searchButton = tk.Button(self.button_frame, text="Wyszukaj książkę", command=self.search_books, width=20, height=2, bg="#ffeb3b", fg="black", font=("Helvetica", 14, "bold"), bd=2, relief="solid", highlightthickness=3, highlightbackground="#fbc02d", highlightcolor="#fbc02d")
        self.searchButton.grid(row=1, column=0, padx=10, pady=10)

        self.quitButton = tk.Button(self.button_frame, text="Wyjdź", command=self.master.destroy, width=20, height=2, bg="#f44336", fg="white", font=("Helvetica", 14, "bold"), bd=2, relief="solid", highlightthickness=3, highlightbackground="#d32f2f", highlightcolor="#d32f2f")
        self.quitButton.grid(row=1, column=1, padx=10, pady=10)

        self.booksList = tk.Listbox(self.main_frame, width=80, height=10, bg="#dff9fb", fg="black", font=("Helvetica", 12))
        self.booksList.pack(pady=10)

    def add_book(self):
        AddBookWindow(self.master, self.biblioteka)

    def view_books(self):
        self.booksList.delete(0, tk.END)
        if not self.biblioteka.ksiazki:
            messagebox.showinfo("Informacja", "Biblioteka jest pusta.")
        else:
            for ksiazka in self.biblioteka.ksiazki:
                self.booksList.insert(tk.END, str(ksiazka))

    def search_books(self):
        SearchBookWindow(self.master, self.biblioteka, self.booksList)
