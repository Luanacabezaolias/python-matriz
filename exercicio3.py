'''Solicite ao usuário 15 valores e armazene em uma matriz 3x5 e exiba a matriz. A seguir, troque todos 
os elementos da matriz que sejam maiores do que 100 pelo valor zero e exiba a matriz novamente'''

import modulo_matriz

matriz = modulo_matriz.preenche_matriz(5, 5)
modulo_matriz.exibe_matriz(matriz)


for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] > 100:
            matriz[i][j] = 0


modulo_matriz.exibe_matriz(matriz)