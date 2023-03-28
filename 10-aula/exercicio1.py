# Definindo Função Tij[l+1] | Diferenças finitas
import matplotlib.pyplot as plt
import numpy as np
WIDTH = 50
HEIGHT = 50
# Definindo Variaveis + Constantes
alpha = 0.25 # Mˆ2/s
l = 0.5
deltaX = 0.01 # cm
deltaY = 0.01 # cm
deltaT = 0.1 # s
T0 = 100 # °C
T10 = 50 # °C
TMax = 10

# Definindo Função
Tempo = int(10/deltaT)
tamanhoX = int(l/deltaX)
tamanhoY = int(l/deltaY)
Temp = np.zeros((Tempo,tamanhoX,tamanhoY))
Temp[:][0][:] = 100

# Definindo Temperatura | Base

for t in range(1, Tempo -1):
    for l in range(1, tamanhoX - 1):
        for c in range(1, tamanhoY - 1):
            diferencialY =(Temp[t][l+1][c] +  Temp[t][l-1][c] - 2 * Temp[t, l,c]) / deltaX ** 2
            diferencialX =(Temp[t][l][c+1] +  Temp[t][l][c-1] - 2 * Temp[t, l,c]) / deltaY ** 2
            diferencialT = diferencialX + diferencialY
            Temp[t + 1][l][c] = Temp[t][l][c] + diferencialT * alpha * deltaT

# PLT Matrix
plt.matshow(Temp[])
plt.show()