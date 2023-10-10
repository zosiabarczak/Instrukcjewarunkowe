#!/usr/bin/env python3

print("Hello, tu mój program") # Wypisz na ekran
wiek = input("Podaj swój wiek\n") # Pobierz ciąg znaków, zwrócona zmina jst typu string 
wiek = int(wiek) # Zrob konwersje typu zmiennej z string na integer 

# Wypisz na ekran użytkownikowi co podał, dokonana jest konwersja typu na string
print("Podałeś, że twój wiek to: " + str(wiek) + ". Nieźle.")

if wiek < 18:
    print('Brawo, jesteś niepełnoletni')
elif wiek < 60:
    print('Juz jestes pełnoletni i możesz pracować')
elif wiek > 60:
    print('Juz jestes na emeruturze')
elif wiek > 100 and wiek < 120:
    print('Uuu, rekord życia')
else:
    print('Chyba coś kłamiesz')
