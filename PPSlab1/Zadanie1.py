import math

def oblicz_pierwiastki(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)
    elif delta == 0:
        x = -b / (2 * a)
        return(x, )
    else:
        return None
while(True):
    a = float(input("Podaj wspolczynnik a: "))
    b = float(input("Podaj wspolczynnik b: "))
    c = float(input("Podaj wspolczynnik c: "))

    pierwiastki = oblicz_pierwiastki(a, b, c)

    if pierwiastki is not None:
        if len(pierwiastki) == 2:
            x1, x2 = pierwiastki
            print(f"Pierwiastki dla takich wspolczynnikow to: {x1} i {x2}")
        else:
            x1, = pierwiastki
            print(f"Pierwiastek dla takich wspolczynnikow to: {x1}")
    else:
        print("Nie ma pierwiastkow dla takich wspolczynnikow")