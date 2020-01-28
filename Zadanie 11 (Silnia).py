n = int(input("Prosze podac liczbe: "))
wybor = int(input("Wybierz 1, aby obliczyc silnie rekurencyjnie. Wybierz 2, aby obliczyc silnie iteracyjnie: " ))


def silnia_rek (n):
    if(n > 1):
        return n*silnia_rek(n - 1) 
    elif(n in (0, 1)): 
        return 1
    else:
      return "Niepoprawna liczba"
        
def silnia_iter (n):
    iteracja = 1
    if( n > 1):
        for i in range (2, n + 1):
            iteracja = iteracja * i
        return iteracja
    elif(n in (0, 1)): 
        return 1
    else:
      return "Niepoprawna liczba"



if (wybor == 1):
    print(silnia_rek(n))
elif(wybor == 2):
    print(silnia_iter(n))
else:
    print("Niepoprawny wybor")

