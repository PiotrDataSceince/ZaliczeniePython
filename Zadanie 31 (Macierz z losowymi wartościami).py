import numpy as np

liczba_N = 4

def losowa_macierz(N):
    return np.random.choice([255, 0], N*N, p=[0.5, 0.5]).reshape(N, N)

a = losowa_macierz(liczba_N)

print(a)