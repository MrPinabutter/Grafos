'''
Estes algoritmos servem apenas para grafos simples, sem arestas paralelas na sua composição.
'''

n = int(input('Quantos vertices tem o seu grafo? '))

grafo = []
# Recebendo o grafo
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
for vertice, vizinhos in enumerate(grafo):
    for vizinho in vizinhos:
        # Verifica se a aresta (vertice, vizinho) ja existe no novo 
        if (vertice, vizinho) not in arestas and (vizinho, vertice) not in arestas:
            peso = float(input(f'Digite o peso dos pares de vertices ({vizinho}, {vertice}): '))
            arestas[(vizinho, vertice)] = peso

print(f'As arestas ligadas com seus respectivos pesos: {arestas}')  # OBS: Ficam de fora os vertices isolados do grafo nesta contagem