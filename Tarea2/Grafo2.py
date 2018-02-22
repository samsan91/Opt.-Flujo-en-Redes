from random import random, choice
from sys import stdout

colores = ["red", "orange"]

def cabecera(aristas, eps=False):
    if eps:
        print("set term postscript eps", file = aristas)
        print("set output 'Grafo2.eps'", file = aristas)
    else:
        print("set term png", file = aristas)
        print("set output 'Grafo2.png'", file = aristas)
    print('set xrange [-0.1:1.1]', file = aristas)
    print('set yrange [-0.1:1.1]', file = aristas)
    print('set size square', file = aristas)
    print('set key off', file = aristas)
    
def inf(destino, aristas):
    print("plot '{:s}' using 1:2 with points pt 7".format(destino), file = aristas)

class Grafo:
    def __init__(self):
        self.n = None # un conjunto de variables sin inicializar
        self.x = dict()
        self.y = dict()
        self.E = []
        self.destino = None
 
    def generar(self, orden): #generando los nodos necesarios
        self.n = orden
        for nodo in range(self.n):
            self.x[nodo] = random() 
            self.y[nodo] = random() 
        
 
    def imprimir(self, direccion): #se guardan "x" y "y" en archivo
        self.destino = direccion
        with open(self.destino, "w") as archivo:
            for nodo in range(self.n):
                print(self.x[nodo], self.y[nodo], file=archivo)
        print(self.destino)
        
    def conectar(self, probabilidad): # conectar nodos y aristas
        for nodo in range(self.n - 1):
            for nodo2 in range(nodo + 1, self.n):
                if random() < probabilidad:
                    color = choice(colores)
                    self.E.append((nodo, nodo2, color))
        print(len(self.E))
        
    def graficar (self, plot): #crear el grafo en gnuplot
        assert self.destino is not None
        with open(plot, "w") as aristas:
            cabecera(aristas)
            num = 1
            for(v, w, c) in self.E:
                x1 = self.x[v]
                x2 = self.x[w]
                y1 = self.y[v]
                y2 = self.y[w]
                print("set arrow {:d} from {:f}, {:f} to {:f}, {:f} lw 2 lt 5 lc rgb 'red' nohead".format(num,x1,y1,x2,y2), file = aristas)
                num += 1
                inf(self.destino, aristas)






                
