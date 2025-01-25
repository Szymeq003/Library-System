# System Biblioteczny

## Opis
Projekt "System Biblioteczny" to aplikacja napisana w Pythonie z wykorzystaniem biblioteki Tkinter do stworzenia graficznego interfejsu użytkownika (GUI). Aplikacja umożliwia dodawanie, wyświetlanie i wyszukiwanie książek w bibliotece.

## Funkcjonalności
- **Dodaj książkę**: Umożliwia dodanie nowej książki do biblioteki.
- **Wyświetl wszystkie książki**: Wyświetla wszystkie książki w bibliotece.
- **Wyszukaj książkę**: Umożliwia wyszukiwanie książek na podstawie tytułu, autora lub roku wydania.

## Wymagania
- Python 3.7 lub nowszy
- `tkinter` (wbudowane w standardową dystrybucję Pythona)
- `Pillow` (do obsługi obrazów)

## Instalacja
1. **Klonowanie repozytorium**:
    ```sh
    git clone https://github.com/Szymeq003/Library-System.git
    cd Library-System
    ```

2. **Instalacja zależności**:
    Jeśli korzystasz z narzędzia `poetry`, wykonaj:
    ```sh
    poetry install
    ```

    Lub, jeśli używasz `pip`, wykonaj:
    ```sh
    pip install -r requirements.txt
    ```

3. **Uruchomienie aplikacji**:
    ```sh
    poetry run python main.py
    ```

    Lub, jeśli używasz `pip`, wykonaj:
    ```sh
    python main.py
    ```

## LibrarySystem/
    ├── setup.py
    ├── library_system/
    │   ├── __init__.py
    │   ├── book.py
    │   ├── library.py
    │   ├── add_book_window.py
    │   ├── search_book_window.py
    │   └── application.py
    └── main.py



## Jak korzystać
1. **Dodaj książkę**:
    - Kliknij przycisk "Dodaj książkę".
    - Wprowadź tytuł, autora i rok wydania.
    - Kliknij przycisk "Dodaj".

2. **Wyświetl wszystkie książki**:
    - Kliknij przycisk "Wyświetl wszystkie książki".
    - Zostaną wyświetlone wszystkie książki w bibliotece.

3. **Wyszukaj książkę**:
    - Kliknij przycisk "Wyszukaj książkę".
    - Wprowadź słowo kluczowe (tytuł, autor lub rok).
    - Kliknij przycisk "Szukaj".
    - Zostaną wyświetlone wyniki wyszukiwania.

## Autorzy
- [Szymon Pyrz](https://github.com/Szymeq003)

## Licencja
Ten projekt jest licencjonowany na warunkach licencji MIT. Zobacz plik [LICENSE](LICENSE) w repozytorium, aby uzyskać więcej informacji.
