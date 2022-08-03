# Program pobiera wyraz z Pliku tekstowego
import random
with open ("Hasla.txt" , "r") as file:
    allText = file.read()
    words = list(map(str,allText.split()))

# zamiana wyrazu z pliku tekstowego na hasło
hasło = random.choice(words)
tablica = list(hasło)

# tablica służy do wyświetlania * * * * *
for i in range(len(hasło)):
    tablica[i] = "*"

# zmienna żyć
życia = 10

# pętla while, w której będzie realizowana gra
while życia > 0:
    print('')
    print('Masz jeszcze: ', życia, 'żyć')
    print('')
    print(' '.join(tablica))
    print('')

    # podaj litere
    print('podaj literę')
    litera = input()

    # udana próba
    if litera in hasło:
        # zmiena - na litere
        for i in range(len(tablica)):
            if (hasło[i] == litera):
                tablica[i] = litera

        # Sprawdzarka do odgadnietego wyrazu
        if litera == hasło:
            print('Wygrałeś :D')
            break

        # Sprawdzarka do litery wyrazu
        if ''.join(map(str, tablica)) == hasło:
            print('Wygrałeś :D')
            break

    # nie udana próba
    else:
        życia = życia - 1
    if życia == 0: print('coś się nie udało :///')