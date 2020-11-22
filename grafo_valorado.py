class Aresta():
    def __init__(self, value, vertexs):
        self.value = value 
        self.vertexs = vertexs

a1 = Aresta(1, [1, 2])
a2 = Aresta(2, [2, 3])
a3 = Aresta(3, [3, 4])
a4 = Aresta(9, [1, 3])
a5 = Aresta(9, [4, 5])
a6 = Aresta(4, [5, 6])
a7 = Aresta(5, [3, 5])
a8 = Aresta(8, [1, 4])

grafo_valorado = [a1, a2, a3, a4, a5, a6, a7, a8]

def buscaArestas(grafo, vertice):
    lista = []
    for aresta in grafo:
        if vertice in aresta.vertexs:
            lista.append(aresta)
            print(aresta.vertexs)
    return lista

# Testando o algoritmo de prim (falta terminar)
def Prim(grafo, vertice, passou, extremidades):
    arestas = buscaArestas(grafo, vertice)
    for idx, aresta in enumerate(arestas):
        if idx == 0:
            maior = aresta
        if aresta.value > maior:
            maior = aresta
    passou.append(aresta)
    

buscaArestas(grafo_valorado, 1)