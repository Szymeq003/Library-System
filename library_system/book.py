class Ksiazka:
    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok

    def __str__(self):
        return f"'{self.tytul}' autorstwa {self.autor} ({self.rok})"
