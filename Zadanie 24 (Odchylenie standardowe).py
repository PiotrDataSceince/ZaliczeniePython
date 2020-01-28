lista = [0.5, 0.4, 0.3, 1.3, 1.4]


def odchylenie_standardowe(x):
     sr = sum(x) / len(x)
     suma = 0
     for i in range(len(x)-1):
       suma = suma + (x[i] - sr)**2
     wariancja = suma/len(x)
     return wariancja**0.5
 
a = odchylenie_standardowe(lista)

print(a)
