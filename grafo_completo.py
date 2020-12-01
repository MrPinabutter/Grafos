n = int(input('Quantos vertices tem o seu grafo? '))

grafo = []
for i in range(n):
    vizinhos = input(f'Digite os todos vizinhos, separado por espaço, do vertice {i}: ').split(' ')
    if vizinhos == ['']:
        vizinhos = [i]
    else:
        vizinhos = [int(x) for x in vizinhos]
    grafo.append(vizinhos)

print(f'Seu Grafo: {grafo}')

def isConectado(grafo, vertice, visitados):
    visitados.append(vertice)
    cont = 0
    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            isConectado(grafo, vizinho, visitados)
    return len(visitados) == len(grafo)
print('O grafo é conectado' if isConectado(grafo, 0, []) else 'O grafo não é conectado')

    