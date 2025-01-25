import tkinter as tk

class SearchBookWindow(tk.Toplevel):
    def __init__(self, master, biblioteka, books_list):
        super().__init__(master)
        self.title("Wyszukiwanie książki")
        self.configure(bg="#e0f7fa")
        self.biblioteka = biblioteka
        self.books_list = books_list
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the form
        search_frame = tk.Frame(self, padx=10, pady=10, bg="#e0f7fa")
        search_frame.pack(fill=tk.BOTH, expand=True)

        # Add label and entry for search query
        self.search_label = tk.Label(search_frame, text="Wpisz słowo kluczowe (tytuł, autor lub rok):", bg="#e0f7fa", font=("Helvetica", 12))
        self.search_label.grid(row=0, column=0, pady=5)
        self.search_entry = tk.Entry(search_frame, font=("Helvetica", 12))
        self.search_entry.grid(row=0, column=1, pady=5)

        # Add search button
        self.search_button = tk.Button(search_frame, text="Szukaj", command=self.submit_search, bg="#4caf50", fg="white", font=("Helvetica", 12, "bold"), relief=tk.FLAT)
        self.search_button.grid(row=1, columnspan=2, pady=10)

    def submit_search(self):
        zapytanie = self.search_entry.get()
        self.books_list.delete(0, tk.END)
        if zapytanie:
            wyniki = [
                ksiazka for ksiazka in self.biblioteka.ksiazki
                if zapytanie.lower() in ksiazka.tytul.lower() or zapytanie.lower() in ksiazka.autor.lower() or zapytanie in str(ksiazka.rok)
            ]
            if wyniki:
                for ksiazka in wyniki:
                    self.books_list.insert(tk.END, str(ksiazka))
                self.destroy()
            else:
                messagebox.showinfo("Wyniki wyszukiwania", f"Nie znaleziono książek pasujących do '{zapytanie}'.")
