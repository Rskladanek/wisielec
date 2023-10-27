# Gra Wieszak - Wisielec w Pythonie

## Opis

Gra "Wieszak" to prosty projekt napisany w Pythonie, który pozwala graczowi odgadywać losowo wybrane słowo z pliku tekstowego. Gracz ma ograniczoną liczbę prób, aby odgadnąć słowo litera po literze. Jeśli gracz wykorzysta wszystkie próby, gra się kończy.

## Funkcje

- Losowe wybieranie słowa z pliku tekstowego.
- Dynamiczne wyświetlanie postępu gracza (odgadnięte litery są wyświetlane, niewiadome litery są zastępowane gwiazdkami).
- Licznik "żyć" informujący gracza, ile prób mu pozostało.
- Informacja o wygranej lub przegranej po zakończeniu gry.

## Instrukcja instalacji

1. Sklonuj repozytorium do swojego lokalnego środowiska:
   ```bash
   git clone https://github.com/Rskladanek/wisielec
   ```

2. Przejdź do folderu z projektem:
   ```bash
   cd wisielec
   ```


3. Uruchom program:
   ```bash
   python main.py
   ```

## Jak grać

1. Po uruchomieniu programu zostaniesz poproszony o podanie litery.
2. Twoim celem jest odgadnięcie całego słowa przed wykorzystaniem wszystkich prób.
3. Po każdej nieudanej próbie liczba pozostałych "żyć" będzie się zmniejszać.
4. Gra kończy się, gdy odgadniesz całe słowo lub wykorzystasz wszystkie próby.

## Dodatkowe informacje

Jeśli chcesz dodać więcej słów do gry, po prostu edytuj plik `Hasla.txt` i dodaj nowe słowa, każde w nowej linii.
