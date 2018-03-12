
from Grafo2 import Grafo
Grafo = Grafo()
Grafo.generar(7)
Grafo.imprimir("test.txt")
Grafo.conectar(0.5)
Grafo.graficar("test.plot",3)
G= Grafo.floyd_warshall()
print(G)
