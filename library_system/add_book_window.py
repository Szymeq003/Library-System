import tkinter as tk
from tkinter import messagebox

class AddBookWindow(tk.Toplevel):
    def __init__(self, master, biblioteka):
        super().__init__(master)
        self.title("Dodaj książkę")
        self.configure(bg="#e0f7fa")
        self.biblioteka = biblioteka
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the form
        form_frame = tk.Frame(self, padx=10, pady=10, bg="#e0f7fa")
        form_frame.pack(fill=tk.BOTH, expand=True)

        # Add label and entry for title
        self.title_label = tk.Label(form_frame, text="Tytuł", bg="#e0f7fa", font=("Helvetica", 12))
        self.title_label.grid(row=0, column=0, pady=5)
        self.title_entry = tk.Entry(form_frame, font=("Helvetica", 12))
        self.title_entry.grid(row=0, column=1, pady=5)

        # Add label and entry for author
        self.author_label = tk.Label(form_frame, text="Autor", bg="#e0f7fa", font=("Helvetica", 12))
        self.author_label.grid(row=1, column=0, pady=5)
        self.author_entry = tk.Entry(form_frame, font=("Helvetica", 12))
        self.author_entry.grid(row=1, column=1, pady=5)

        # Add label and entry for year
        self.year_label = tk.Label(form_frame, text="Rok wydania", bg="#e0f7fa", font=("Helvetica", 12))
        self.year_label.grid(row=2, column=0, pady=5)
        self.year_entry = tk.Entry(form_frame, font=("Helvetica", 12))
        self.year_entry.grid(row=2, column=1, pady=5)

        # Add submit button
        self.submit_button = tk.Button(form_frame, text="Dodaj", command=self.submit_book, bg="#4caf50", fg="white", font=("Helvetica", 12, "bold"), relief=tk.FLAT)
        self.submit_button.grid(row=3, columnspan=2, pady=10)

    def submit_book(self):
        tytul = self.title_entry.get()
        autor = self.author_entry.get()
        rok = self.year_entry.get()
        if tytul and autor and rok:
            self.biblioteka.dodaj_ksiazke(tytul, autor, rok)
            self.destroy()
        else:
            messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione.")
