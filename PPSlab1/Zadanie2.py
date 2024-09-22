def zlicz_znaki(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        tekst = plik.read()

    wystapienia = {}

    for znak in tekst:
        znak_lower = znak.lower()
        if znak_lower != ' ' and znak_lower != '\n':
            if znak_lower in wystapienia:
                wystapienia[znak_lower] += 1
            else:
                wystapienia[znak_lower] = 1
    wystapienia_sort = dict(sorted(wystapienia.items()))
    return wystapienia_sort

nazwa_pliku = input("Podaj nazwe pliku: ")
wynik = zlicz_znaki(nazwa_pliku)

for znak, ilosc in wynik.items():
    print(f"{znak}: {ilosc}")