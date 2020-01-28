import numpy as np


def losowa_macierz(n):
    return np.random.choice([255,0], size=n**2, p=[0.4,0.6]).reshape(n,n)

def dodaj_szybowiec(i, j, grid):
    szybowiec = np.array([[0, 0, 255], [255, 0, 255], [0, 255, 255]])
    grid[i:i+3, j:j+3] = szybowiec
    return grid

def dodaj_bochenek(i,j,grid):
    bochenek = np.array([[0,255,255,0],[255,0,0,255],[0,255,0,255],
                      [0,0,255,0]])
    grid[i:i+4, j:j+4] = bochenek
    return grid

def dodaj_cegla(i,j,grid):
    cegla = np.array([[255,255],[255,255]])
    grid[i:i+2, j:j+2] = cegla
    return grid

def dodaj_ul(i,j,grid):
    ul = np.array([[0,255,255,0],[255,0,0,255],[0,255,255,0]])
    grid [i:i+3,j:j+4] = ul
    return grid

def dodaj_lodz(i,j,grid):
    lodz = np.array([[255,255,0],[255,0,255],[0,255,0]])
    grid [i:i+3,j:j+3] = lodz
    return grid

def dodaj_swiatla(i,j,grid):
    swiatla = np.array([[255],[255],[255]])
    grid [i:i+3,j:j] = swiatla
    return grid

def dodaj_zaba(i,j,grid):
    zaba = np.array([[0,255,255,255],[255,255,255,0]])
    grid [i:i+2,j:j+4] = zaba
    return grid

def dodaj_bekon(i,j,grid):
    bekon = np.array([[255,255,0,0],[255,0,0,0],[0,0,0,255],[0,0,255,255]])
    grid [i:i+4,j:j+4] = bekon
    return grid