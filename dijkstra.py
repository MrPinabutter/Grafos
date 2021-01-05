# Recebe o numero de vertice, numerados de 0 a n
n = int(input('Quantos vertices tem o seu grafo? '))

grafo = []
# Recebendo os vizinhos de cada vertice
for i in range(n):
    vizinhos = input(f'Digite os todos vizinhos, separado por espaço, do vertice {i}: ').split(' ')
    if vizinhos == ['']:
        vizinhos = []
    else:
        vizinhos = [int(x) for x in vizinhos]
    grafo.append(vizinhos)

print(f'Seu Grafo: {grafo}')

arestas = {}

# Adicionando pesos ao grafo
print("Formato = (origem, destino)")
for vertice, vizinhos in enumerate(grafo):
    for vizinho in vizinhos:
        # Verifica se a aresta (vertice, vizinho) ja existe no novo 
        if (vertice, vizinho) not in arestas:
            peso = float(input(f'Digite o peso dos pares de vertices ({vertice}, {vizinho}): '))
            arestas[(vertice, vizinho)] = peso

print(f'As arestas ligadas com seus respectivos pesos: {arestas}') 

def dijkstra