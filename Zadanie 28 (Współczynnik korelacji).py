lista_x = [55, 21, 35, 58, 28, 30, 32, 20, 35, 46, 34, 53, 30]
lista_y = [5, 1, 2, 2, 1, 2, 3, 0, 0, 0, 2, 0, 4]

def sr_x(x):
    return sum(x) / len(x)

def sr_y(y):
    return sum(y) / len(y)

def szereg_licznik(x, y):
    aryt_x = sr_x(x)
    aryt_y = sr_y(y)
    szereg = 0
    for i in range (len(x)):
        szereg = szereg + (x[i] - aryt_x) * (y[i] - aryt_y)
    return szereg

def szereg_mianownik_x(x):
    aryt_x = sr_x(x)
    szereg = 0
    for i in range(len(x)):
        szereg = szereg + (x[i] - aryt_x)**2
    return szereg

def szereg_mianownik_y(y):
    aryt_y = sr_y(y)
    szereg = 0
    for i in range(len(y)):
        szereg = szereg + (y[i] - aryt_y)**2
    return szereg


def wspolczynnik_korelacji(x, y):
    return szereg_licznik(x, y)/(szereg_mianownik_x(x) * szereg_mianownik_y(y)) ** 0.5

a = wspolczynnik_korelacji(lista_x, lista_y)

print(a)
     

