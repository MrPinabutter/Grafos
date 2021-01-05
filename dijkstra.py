# Recebe o numero de vertice, numerados de 0 a n
n = int(input('Quantos vertices tem o seu grafo? '))
grafo = {}
# Recebendo os vizinhos e pesos de cada vertice
for i in range(n):
    pesos = []
    vizinhos = input(f'Digite os todos vizinhos, separado por espaço, do vertice {i}: ').split(' ')
    for vizinho in vizinhos:
        value = int(input(f'Digite o peso da aresta ({i}, {vizinho}): '))
        pesos.append(value)
    if vizinhos == ['']:
        vizinhos = []
    else:
        vizinhos = [x for x in vizinhos]

    grafo[f'{i}'] = {x: pesos[y] for y, x in enumerate(vizinhos)}

print("Grafo: ",grafo)

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

        for no in nosRestantes:
            if noMaisCurto is None:
                noMaisCurto = no
            elif menorDistancia[no] < menorDistancia[noMaisCurto]:
                noMaisCurto = no
        
        caminhosPossiveis = grafo[noMaisCurto].items()

        for noFilho, peso in caminhosPossiveis:
            if peso + menorDistancia[noMaisCurto] < menorDistancia[noFilho]:
                menorDistancia[noFilho] = peso + menorDistancia[noMaisCurto]
                track[noFilho] = noMaisCurto
        
        nosRestantes.pop(noMaisCurto)

    noAtual = destino

    while noAtual != str(origem):
        try:
            caminho.insert(0, noAtual)
            noAtual = track[noAtual]
        except KeyError:
            print("Impossivel chegar ao destino")
            break

    caminho.insert(0, origem)

    if menorDistancia[str(destino)] < float('inf'):
        print("Distancia mais curta é ", menorDistancia[str(destino)])
        print('Caminho ', caminho)
a = input('Digite a origem de busca: ')
b = input('Digite o destino: ')
dijkstra(grafo, a, b)