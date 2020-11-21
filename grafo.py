class Vertex():
  def __init__(self, value):
    self.value = value
    self.neighbors = []

# Definindo os vertices
a = Vertex(1)
b = Vertex(2)
c = Vertex(3)
d = Vertex(4)
e = Vertex(5)
f = Vertex(6)

# Definindo os vizinhos
a.neighbors = [2, 4]
b.neighbors = [1, 3]
c.neighbors = [2, 4, 5]
d.neighbors = [1, 3, 5]
e.neighbors = [3, 4]
f.neighbors = [5]

grafo = [a, b, c, d, e, f]

# Encontrando o vertice pelo index
def buscaVertex(vertice, grafo):
  for v in grafo:
    if v.value == vertice:
      return v
  return []

# Buscando um caminho a partir de um vertice
def caminho(grafo, vertice, visitados):
  # Encontrando o objeto vertex
  vertex = buscaVertex(vertice, grafo)
  print(vertex.value, end=' ')

  # Adicionando aos percorridos
  visitados.append(vertice)

  # Buscando um caminho por ele
  for i in vertex.neighbors:
    if i not in visitados:
      visitados.append(i)
      caminho(grafo, i, visitados)

caminho(grafo, 1, [])