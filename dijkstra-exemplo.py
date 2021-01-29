import time

def dijkstra(grafo, origem, destino):
    menorDistancia = {}
    track = {}
    nosRestantes = grafo
    infinito = float('inf')
    caminho = []

    # Inicializando a distancia infinita para cada nó
    for no in nosRestantes:
        menorDistancia[no] = infinito
    menorDistancia[str(origem)] = 0
    
    # Loop até que todos os nós sejam vizitados
    while nosRestantes:
        noMaisCurto = None
        
        # Procurando o menor nó do grafo
        for no in nosRestantes:
            if noMaisCurto is None:
                noMaisCurto = no
            elif menorDistancia[no] < menorDistancia[noMaisCurto]:
                noMaisCurto = no
        
        # Olha os vizinhos do grafo mais curto
        caminhosPossiveis = grafo[noMaisCurto].items()

        # Mede os pesos entre o menor nó e os seus vizinhos
        for noFilho, peso in caminhosPossiveis:
            if peso + menorDistancia[noMaisCurto] < menorDistancia[noFilho]:
                menorDistancia[noFilho] = peso + menorDistancia[noMaisCurto]
                track[noFilho] = noMaisCurto
        
        # Remove o no do grafo
        nosRestantes.pop(noMaisCurto)

    noAtual = destino

    # Gerando caminho se possivel fazendo um trackback do caminho dos nós
    while noAtual != str(origem):
        try:
            caminho.insert(0, noAtual)
            noAtual = track[noAtual]
        except KeyError:
            print("Impossivel chegar ao destino")
            break

    caminho.insert(0, origem)

    print(f'Menor distancia de cada vertice {menorDistancia}')
    print('-' * 50)
    for valor, origem in track.items():
        print(f'{origem} -> {valor}')
    print('-' * 50)
    

    if menorDistancia[str(destino)] < float('inf'):
        print("Distancia mais curta é ", menorDistancia[str(destino)])
        print('Caminho ', caminho)

grafo = {
    '0': {'1': 1, '2': 5},
    '1': {'2': 3},
    '2': {'3': 2, '4': 6},
    '3': {'4': 3, '5': 2, '9': 1},
    '4': {'1': 4},
    '5': {'6': 1, '7': 5, '8': 4, '9': 3},
    '6': {'4': 3, '7': 3},
    '7': {'8': 8},
    '8': {'9': 5},
    '9': {'9': 2},
}

inicio = time.time()
dijkstra(grafo, '0', '9')
fim = time.time()
print(f'Tempo de execução: {fim - inicio}')
