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
print()

def isConectado(grafo, vertice, visitados):
    visitados.append(vertice)
    cont = 0
    # Percorre um caminho por todos os vizinhos do vertice inicial
    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            isConectado(grafo, vizinho, visitados)
    return len(visitados) == len(grafo)

print('O grafo é conectado' if isConectado(grafo, 0, []) else 'O grafo não é conectado')
print()

def isRegular(grafo):
    val = 0
    if len(grafo) == 1:
        return True
    # Verifica se todos os vertices tem o mesmo grau
    for i, vizinhos in enumerate(grafo):
        n = 0
        if i == 0:
            val = len(vizinhos)
            continue
        n = len(vizinhos)
        if val != n:
            return False
    return True
        
print('O grafo é regular' if isRegular(grafo) else 'O grafo não é regular')
print('-='*27)
print('Agora vamos comparar seu grafo com o outro a seguir')
print('-='*27)

n = int(input('Quantos vertices tem o seu subgrafo? '))

grafo2 = {}
# Recebendo o grafo2
for i in range(n):
    vert = int(input('Digite o indice do vertice: '))
    vizinhos = input(f'Digite os todos vizinhos, separado por espaço, do vertice {vert}: ').split(' ')
    if vizinhos == ['']:
        vizinhos = []
    else:
        vizinhos = [int(x) for x in vizinhos]
    grafo2[vert] = vizinhos


print(f'Seu outro grafo: {grafo2}')


def isSubgrafo(grafo1, grafo2):
    for v in grafo2.items():    # v[0] = vertice v[1] = vizinhos
        # Verificando se o grafo origem contem o vertice do grafo2
        if v[0] > len(grafo1):
            return False
        
        # Verificando se as arestas do grafo2 existem no grafo1
        for i in v[1]:
            if i not in grafo1[v[0]]:
                return False
    return True

print(f'É um subgrafo do primeiro' if isSubgrafo(grafo, grafo2) else 'Não é subgrafo')