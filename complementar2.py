'''Preencha uma matriz 5x5 e informe se essa matriz é ou não simétrica. Uma matriz é considerada simétrica 
quando ela é igual a sua transposta.'''

from modulo_matriz import preenche_matriz, exibe_matriz

matriz = preenche_matriz(5,5)
exibe_matriz(matriz)

transposta = []
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[0])):
        linha.append(matriz[j][i])
    transposta.append(linha)
exibe_matriz(transposta)

if matriz == transposta:
    print("A matriz é simétrica.")
else: 
    print("A matriz é assimétrica.")