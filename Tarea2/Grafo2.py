from random import random, choice
from sys import stdout

colores = ["red", "orange", "black", "blue", "brown","pink", "gray", "green", "purple", "red"]

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
    print("plot '{:s}' using 1:2:(rand(0)) with points pt 7 lc palette".format(destino), file = aristas)

class Grafo:
    def __init__(self):
        self.n = None # Un conjunto de variables sin inicializar
        self.x = dict()
        self.y = dict()
        self.E = [] # Vacío
        self.destino = None
 
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






                
