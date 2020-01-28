lista = [0.5, 0.4, 0.3, 1.3, 1.4]


def mediana(x):
    x.sort()
    index = float(len(x) + 1)
    if (len(x) % 2 == 0):
      mediana_parz =  (len(x)/2 + index/2) / 2
      return mediana_parz
    else:
        mediana_nieparz = index/2
        return mediana_nieparz
    

a  = mediana(lista)

print(a)