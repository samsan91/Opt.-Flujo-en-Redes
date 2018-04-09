
from Grafo2 import Grafo
from datetime import datetime
from time import clock
print("------------Grafos-------------")
n = 20
p = 0

resultadosFF = []
cantidadCorridas = 20
with open("tiemposFFyFW.txt", "a") as f:
    
    for t in range(cantidadCorridas):
        Grafo = Grafo()
        Grafo.generar(n)
        Grafo.imprimir("test.txt")
        E = Grafo.conectar(0.5)
        Grafo.graficar("test.plot",3)
        Grafo.FloydWarshall()
        print("Resultado FloydWarshall")
        print(Grafo.FloydWarshall())
        
        tiempoFloyd = clock() - InicialFloyd
        print("Tiempo de ejecucion FloydWarshall:")
        print(tiempoFloyd)

        InicialFord = clock()
        a = Grafo.FordFulkerson(1,n - 1)
        FinalFord = clock()
        tiempoFord = clock() - InicialFord
        print("Tiempo de ejecucion FordFulkerson:")
        print(tiempoFord)
        print("FordFulkerson desde el inicio")
        print(a)
        p = p + 1
        n = n + 10
        print("---------------------------------------------------------" + str(p))
        print("Valores de N + 10:")
        print(n)

        resultadosFF.append(a)
        f.write('{}, {}, {} \n'.format(n, tiempoFloyd, tiempoFord))

print("Flujos Maximos por corridas:")
print(resultadosFF)

    
