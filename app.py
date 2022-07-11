# Importamos librerias
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# leer fichero
leer = pd.read_csv("titanic_dataset.csv") 
print(leer)

#elimina las filas duplicadas 
leer = leer.drop_duplicates()
print(leer)

#Elimina vacias
leer = leer.dropna()


# graficos

xpoints = np.array(leer['Survived'])
ypoints = np.array(leer['Pclass'])

plt.plot(xpoints, ypoints, 'o')
plt.show()