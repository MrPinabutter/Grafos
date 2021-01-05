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

print(grafo)

def dijkstra():
    pass
