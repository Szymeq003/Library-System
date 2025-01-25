from .book import Ksiazka

class Biblioteka:
    def __init__(self):
        self.ksiazki = []

    def dodaj_ksiazke(self, tytul, autor, rok):
        try:
            if not tytul or not autor or not rok:
                raise ValueError("Wszystkie pola (tytuł, autor, rok) muszą być wypełnione.")
            if not rok.isdigit() or int(rok) < 0:
                raise ValueError("Rok musi być liczbą dodatnią.")
            ksiazka = Ksiazka(tytul, autor, int(rok))
            self.ksiazki.append(ksiazka)
            print(f"Książka '{tytul}' została pomyślnie dodana!")
        except ValueError as e:
            print(f"Błąd: {e}")

    def wyswietl_ksiazki(self):
        if not self.ksiazki:
            print("Biblioteka jest pusta.")
        else:
            print("\nKsiążki w bibliotece:")
            for ksiazka in self.ksiazki:
                print(ksiazka)

    def wyszukaj_ksiazki(self, zapytanie):
        zapytanie = zapytanie.lower()
        wyniki = [
            ksiazka for ksiazka in self.ksiazki
            if zapytanie in ksiazka.tytul.lower() or zapytanie in ksiazka.autor.lower() or zapytanie in str(ksiazka.rok)
        ]
        if wyniki:
            print("\nWyniki wyszukiwania:")
            for ksiazka in wyniki:
                print(ksiazka)
        else:
            print(f"Nie znaleziono książek pasujących do '{zapytanie}'.")
