from random import randint

def preenche_matriz(lin: int, col: int) -> list:
    '''Prenche a matriz com entrada do usuario'''
    matriz = []
    for i in range(lin):
        linha = []
        for j in range(col):
            n = int(input('Número: '))
            linha.append(n)
        matriz.append(linha)
    return matriz

def preencher_matriz_aleatoria(lin: int, col: int) -> list:
    #preencher a matriz com numeros aleatorios 
    matriz = []
    for i in range(lin):      # linha
        linha = []      
        for j in range(col):      # coluna
            n = randint(1, 50)
            linha.append(n)
        matriz.append(linha)
    return matriz

def preencher_matriz_aleatoria_diferente(lin: int, col: int) -> list:
    #preencher a matriz com numeros aleatorios 
    matriz = []
    sorteados = []
    for i in range(lin):      # linha
        linha = []      
        for j in range(col):      # coluna
            n = randint(1, 25)
            while n in sorteados:
                n = randint(1, 25)
            linha.append(n)
            sorteados.append(n)
        matriz.append(linha)
    return matriz

def exibe_matriz(matriz) -> None:
    '''imprime a matriz'''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end='\t')
        print()