from random import random, choice
from sys import stdout
import time

time_ejecucion = 0
print(time_ejecucion)

colores = ["red", "orange", "black", "blue", "brown","pink", "gray", "green", "purple", "red"]

def cabecera(aristas, eps=False):
    if eps:
        print("set term postscript eps enhanced color", file = aristas)
        print("set output 'Grafo2.eps'", file = aristas)
    else:
        print("set term postscript eps enhanced color", file = aristas)
        print("set output 'Grafo2.eps'", file = aristas)
    print('set xrange [-0.1:1.1]', file = aristas)
    print('set yrange [-0.1:1.1]', file = aristas)
    print('set size square', file = aristas)
    print('set key off', file = aristas)
    
def inf(destino, aristas):
    print("plot '{:s}' using 1:2:(rand(0)) with points pt 7 lc palette".format(destino), file = aristas)

class Grafo:
    def __init__(self):
        self.n = None # Un conjunto de variables sin inicializar
        self.x = dict()
        self.y = dict()
        self.E = []
        self.destino = None
        self.vecinos = dict()
        self.i = None
 
    def generar(self, orden): #generando los nodos necesarios
        self.n = orden # Se da una asignación a la variable n
        for nodo in range(self.n):
            self.x[nodo] = random() 
            self.y[nodo] = random()
        
 
    def imprimir(self, direccion): #se guardan "x" y "y" en archivo
        self.destino = direccion
        with open(self.destino, "w") as archivo:
            for nodo in range(self.n):
                print(self.x[nodo], self.y[nodo], file=archivo)
        print(self.destino)
        
    def conectar(self, probabilidad): # Conectar nodos y aristas.
        for nodo in range(self.n - 1):
            for nodo2 in range(nodo + 1, self.n):
                if random() < probabilidad: #Probabilidad de unión de nodos.
                    self.E.append((nodo, nodo2))
            print(len(self.E))


        
    def graficar (self, plot, tipo): #crear el grafo en gnuplot
        assert self.destino is not None
        with open(plot, "w") as aristas:
            cabecera(aristas)
            num = 1
            lwindex = 0
            for(v, w) in self.E:
                x1 = self.x[v]
                x2 = self.x[w]
                y1 = self.y[v]
                y2 = self.y[w]
                weight = int(random()*5 + 1)
                color = int(random()*10)
                if tipo == 0:
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead lw 1 lc rgb '{:s}'".format(num,x1,y1,x2,y2,colores[color]), file = aristas)

                if tipo == 1:
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head filled lw 1 lc rgb '{:s}'".format(num,x1,y1,x2,y2,colores[color]), file = aristas)

                if tipo == 2:
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} nohead  lw {:d} lc rgb '{:s}'".format(num,x1,y1,x2,y2,weight,colores[color]), file = aristas)
                    
                if tipo == 3:
                    print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} head filled lw {:d} lc rgb '{:s}'".format(num,x1,y1,x2,y2,weight,colores[color]), file = aristas)
                lwindex += 1
                num += 1
            inf(self.destino, aristas)




    def FloydWarshall(self):
        d = {}
        for nodo in range(self.n - 1):
            d[(nodo, nodo)] = 0 # distancia reflexiva es cero
            for (vecino, peso) in self.vecinos[nodo]: # para vecinos, la distancia es el peso
                d[(nodo, vecino)] = peso
        for intermedio in self.vecinos:
            for desde in self.vecinos:
                for hasta in self.vecinos:
                    di = None
                    if (desde, intermedio) in d:
                        di = d[(desde, intermedio)]
                    ih = None
                    if (intermedio, hasta) in d:
                        ih = d[(intermedio, hasta)]
                    if di is not None and ih is not None:
                        c = di + ih # largo del camino via "i"
                        if (desde, hasta) not in d or c < d[(desde, hasta)]:
                            d[(desde, hasta)] = c # mejora al camino actual
        return d


    def camino(self, s, t, f): # construcciÃ³n de un camino aumentante
        cola = [s]
        usados = set()
        camino = dict()
        while len(cola) > 0:
            u = cola.pop(0)
            usados.add(u)
            for (i,w, v, p, c) in self.E:
                if w == u and v not in cola and v not in usados:
                    actual = f.get((u, v), 0)
                    dif = p - actual
                    if dif > 0:
                        cola.append(v)
                        camino[v] = (u, dif)
        if t in usados:
            return camino
        else:
            return None
 
 
 
    def FordFulkerson(self, s, t): # algoritmo de Ford y Fulkerson
        if s == t:
            return 0
        maximo = 0
        f = dict()
        while True:
            aum = self.camino(s, t, f)
            if aum is None:
                break # ya no hay
            incr = min(aum.values(), key = (lambda k: k[1]))[1]
            u = t
            while u in aum:
                v = aum[u][0]
                actual = f.get((v, u), 0) # cero si no hay
                inverso = f.get((u, v), 0)
                f[(v, u)] = actual + incr
                f[(u, v)] = inverso - incr
                u = v
            maximo += incr
        return maximo
        print(maximo)

    def TiempoEjecucion():
        t0 = time.clock()
        for i in xrange(10000000):
            pass
        time_ejecucion = time.clock() - t0 
        print("%.2f sec" % (time.clock() - t0))
        return time_ejecucion

    def test(self,s,t):
        for i in range(10000):
            self.FordFulkerson(self,s,t)
            
        start_time = time()
        test()
        elapsed_time = time() - start_time
        print("Elapsed time: %.10f seconds." % elapsed_time)

print(time_ejecucion)
           
#Documenación, lo que se tuvo que hacer para poder adaptar el codigo de la doctora al mio.
#Revisar para grafos simples y ponderados y si funciona con grafos dirigidos, verificar, si tienen sentido las salidas, entonces llegar a una conclusión,
#poner algun mensaje de advertencia si el usuario trata de meter un grafo dirigido, advertiendole que no funciona.
#Aumentamos el tamaño de la instancia, el tiempo de ejecución aumenta
# Con el programa, se van a ejecutar con muchas instancias, de diferentes tamaños, obtener información cuanto se toma de tiempo para ejecutarse, si tus datos
#son normalmente distribuidos, (poner rayas), si no lo son, poner cajas bigote, realizar prueba estadistica para argumentar.
#y erros bars, agregar 3 columnas, candlesticks, parte baja, parta alta, quartil y mediana, why error boths? como hacerlo, ajusta de curvas, (funcion fit)
# dentro del mismo dato, que tal se ajusta lo teorico con lo practico, realizar una discusión del porque se ven las diferencias, hacer un razonamiento, graficar por
#un lado la cubica y del otro las experimentales
#Controlar el numero de nodos

#NOTA: realizar el listado de x y y, como vector en parejas, modificar.
