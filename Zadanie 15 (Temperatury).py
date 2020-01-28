import numpy as np
import matplotlib.pyplot as plt



temperatury_poznan = [3, 5, 1, 3, 4, 8, 2, 3, 5, 7, 2, 3, 4, 1]
temperatury_krakow = [-2, -3, -3, 0, 5, 4, 1, -3, 5, 8, 6, 6, 7, 4]
temperatury_wroclaw = [4, 4, 5, 3, 4, 1, -1, 0, 1, 2, 2, 5, 7, 4]

dni = ["1 stycznia", "2 stycznia", "3 stycznia", 
       "4 stycznia", "5 stycznia", "6 stycznia", "7 stycznia",
       "8 stycznia", "9 stycznia", "10 stycznia", 
       "11 stycznia", "12 stycznia", "13 stycznia", 
       "14 stycznia"]
miasta = ["Poznań", "Warszawa", "Kraków"]
line_poznan = plt.plot(dni, temperatury_poznan, label="Poznań")
line_krakow = plt.plot(dni, temperatury_krakow, label="Kraków")
line_wroclaw = plt.plot(dni, temperatury_wroclaw, label="Wrocław")
plt.suptitle("Temperatura")
plt.legend()
plt.grid()
plt.show()

