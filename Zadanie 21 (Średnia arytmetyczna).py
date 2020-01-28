import numpy as np

lista = [0.5, 0.4, 0.3, 1.3, 1.4]

def srednia_arytmetyczna(x):
     aryt = sum(x) / len(x)
     return aryt


a = srednia_arytmetyczna(lista)

print(a)
print (np.mean(lista))




