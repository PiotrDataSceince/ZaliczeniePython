import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def losowa_macierz(N):
    return np.random.choice([255, 0], N*N, p=[0.5, 0.5]).reshape(N, N)

def dodaj_szybowiec(i, j, grid):
    szybowiec = np.array([[0, 0, 255], [255, 0, 255], [0, 255, 255]])
    grid[i:i+3, j:j+3] = szybowiec
    
def dodaj_cegla(i, j, grid):
    cegla = np.array([[255, 255], [255, 255]])
    grid[i:i+2, j:j+2] = cegla
    
def dodaj_bochenek(i,j,grid):
    bochenek = np.array([[0,255,255,0],[255,0,0,255],[0,255,0,255],
                      [0,0,255,0]])
    grid[i:i+4, j:j+4] = bochenek
    return grid

def suma_sasiadow(i, j, m):

    total = int((m[i-1, j-1] + m[i-1, j] + m[i-1, j+1] + 
						m[i, j-1] + m[i, j+1] + 
						m[i+1, j-1] + m[i+1, j] + m[i+1, j+1])/255)
    return total

def aktual(matrix):
    
    N = matrix.shape[0]
    
    newmatrix = np.zeros(N*N).reshape(N, N)
    
    for i in range(1, N-1):
        for j in range(1, N-1):
            total = suma_sasiadow(i, j, matrix)
            
            if matrix[i, j] == 255:
                if(total < 2) or (total > 3):
                    newmatrix[i, j] = 0
                else:
                    newmatrix[i, j] = 255
            else:
                if total == 3:
                    newmatrix[i, j] = 255
    
    return newmatrix

obraz = losowa_macierz(20)

for i in range(20):
    
    plt.figure()
    plt.imshow(obraz, cmap = 'Greys')
    plt.savefig("foto_{0}".format(i))
    obraz = aktual(obraz)