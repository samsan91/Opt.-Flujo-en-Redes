from random import random, choice
from sys import stdout
import math
import time

time_ejecucion = 0
print(time_ejecucion)

colores = ["yellow", "blue", "pink", "black", "red"]
pesos = [1,2,3,4,5,6,7,8,9,10]

def cabecera(aristas, eps=True):
    if eps:
        print("set term postscript color eps", file = aristas)
        print("set output 'tarea4.eps'", file = aristas)
    else:
        print("set term png", file = aristas)
        print("set output 'tarea4.png'", file = aristas)
    print("set xrange [-0.1:1]", file = aristas)
    print("set yrange [-0.1:1]", file = aristas)
    print('set size square', file = aristas) 
    print('set key off', file = aristas)

def pie(destino, aristas):
    print("plot '{:s}' using 1:2 with points pt 7  ps 1".format(destino), file = aristas)

class Grafo:
    
    def __init__(self):
        self.n = None # se crean las variables pero aun no se inicializan
        self.x = dict()
        self.y = dict()
        self.theta = None
        self.E = []
        self.destino = None
        self.vecinos = dict()
        self.i = None
        

    def generar(self, orden): # creando los nodos
        with open("NodosWarshall.dat", "w") as crear:
            centro = (0.5, 0.5)
            radio = 0.4
            angulo = (360/i)*(pi/180)
            for n in range(1, i+1):
                x = radio*cos(angulo*n) + centro[0]
                y = radio*sin(angulo*n) + centro[1]
                self.n.append((x,y))
                print(x, y, file = crear)
                if not (x, y) in self.vecinos:
                    self.vecinos[(x,y)] = []

    def imprimir(self, dest):
        self.destino = dest
        with open(self.destino , "w") as archivo:
            for nodo in range(self.n):
               print(self.x[nodo], self.y[nodo], file=archivo)
        print(self.destino)

    def conectar(self, prob):
        self.i = 1
        for nodo in range(self.n - 1):
            for otro in range(nodo + 1, self.n):           
                if random() < prob:                    
                    peso = choice(pesos)
                    color = choice(colores)                    
                    if peso > 0:
                        self.E.append((self.i, nodo, otro, peso, color))
                        self.i += 1
                        if not nodo in self.vecinos: # vecindad de nodo
                            self.vecinos[nodo] = set()
                        if not otro in self.vecinos: # vecindad de otro
                            self.vecinos[otro] = set()    
                        self.vecinos[nodo].add((otro, peso))
                        self.vecinos[otro].add((nodo, peso))
        return len(self.E)                                   
        #print(self.E)
        #print(self.vecinos)
        

    def graficar(self, plot): 
        assert self.destino is not None
        with open(plot, "w") as aristas:
            cabecera(aristas)
            num = 1
            for (num,v, w, p, c) in self.E:                
                x1 = self.x[v]
                x2 = self.x[w]
                y1 = self.y[v]
                y2 = self.y[w]              
                flecha = "set arrow {:d} from {:f}, {:f} to {:f}, {:f} lt 5 lw {:f} lc rgb '{:s}' nohead".format(num,x1,y1,x2,y2,p,c)
                #flecha = "set arrow " + srt(num) + "from " + str(x1) + "," + str(y1) + " to " + str(x2) + "," + str(y2) + " lt 5 lw {:f} lc rgb '{:s}' head".format(num,p,c)
               #print(flecha, file=aristas)
                num += 1               
            pie(self.destino, aristas)

    def FloydWarshall(self):
        d = {}
        for nodo in range(self.n - 1):
            d[(nodo, nodo)] = 0 
            for (vecino, peso) in self.vecinos[nodo]: 
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
                            d[(desde, hasta)] = c 
                
        return d
