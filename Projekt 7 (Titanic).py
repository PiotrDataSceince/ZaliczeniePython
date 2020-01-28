import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


titanic_data = pd.read_csv(r"C:\Users\Piotr\Desktop\Studia\Python\Zaliczenie\Projekty\Titanic.csv")

sns.set_style('darkgrid')
histogram_wiek=titanic_data['Age'].hist(bins=20)
calosciowy_stosunek = titanic_data.plot.box(figsize=(10,8))



