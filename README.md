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
    git clone https://github.com/Szymeq003/Library-System
    cd projekt
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

## Struktura projektu
