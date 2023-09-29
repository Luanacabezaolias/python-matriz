'''Uma matriz quadrada é chamada de "quadrado mágico" se a soma dos elementos de cada linha, cada coluna 
e a soma dos elementos das diagonais principal e secundária são todos iguais. Escreva um programa que 
preencha uma matriz 4x4 com valores informados pelo usuário e informe se ela é ou não um quadrado 
mágico. '''

from modulo_matriz import exibe_matriz, preenche_matriz

matriz = preenche_matriz(4, 4)
exibe_matriz(matriz)

soma = 0 
