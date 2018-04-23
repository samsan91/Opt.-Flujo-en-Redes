from random import random
from math import sqrt, ceil, sin, cos, pi, floor
from random import randint, uniform, random
import time, random



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
        self.n = [] # se crean las variables pero aun no se inicializan
        self.E = []
        self.destino = None
        self.vecinos = dict()
        self.aristas = dict()
        self.i = None
        

    def generar(self, orden): 
        with open("Nodos.dat", "w") as archivo:
            centro = (0.5, 0.5)
            radio = 0.5
            angulo = (360/orden)*(pi/180)
            for n in range(1, orden+1):
                x = radio*cos(angulo*n) + centro[0]
                y = radio*sin(angulo*n) + centro[1]
                self.n.append((x,y))
                print(x, y, file = archivo)
                if not (x, y) in self.vecinos:
                    self.vecinos[(x,y)] = []

    def conectar(self, k):
        for r in range(1,k+1):
            for j in range(0,i):
                a = self.n[j]
                b = self.n[j-r]
                self.aristas[(a,b)] = self.aristas[(b,a)] = r
                self.vecinos[a].append(b)
                self.vecinos[b].append(a)

    def conectaraleatorio(self, p):
        for (x1,y1) in self.n:
            for (x2,y2) in self.n:
                rand = random.uniform(0,1)
                if rand < p and ((x1,y1),(x2,y2)) not in self.aristas and ((x2,y2),(x1,y1)) not in self.aristas:
                    self.kmax = floor(i/2)
                    u = self.n.index((x1,y1))
                    v = self.n.index((x2,y2))
                    dis = abs(u-v)
                    if dis > self.kmax:
                        dis2 = i - dis
                        self.aristas[((x1,y1),(x2,y2))] = self.aristas[((x2,y2),(x1,y1))] = dis2
                    else:
                        self.aristas[((x1,y1),(x2,y2))] = self.aristas[((x2,y2),(x1,y1))] = dis                       
                    self.vecinos[(x1,y1)].append((x2,y2))
                    self.vecinos[(x2,y2)].append((x1,y1))

    def distancia(self):
        self.s = floor((3*Tk)-(i/4))
        with open ("Distancia.txt", "w") as distancia:
            self.sumDis = 0
            for u in self.d:
                self.sumDis = self.sumDis + self.d[u]
            self.avgDis = self.sumDis/len(self.d)
            self.DisNormalizada = self.avgDis / self.s
            print(self.DisNormalizada, file = distancia)

    def densidad(self):
        with open ("Densidad.txt", "w") as crear:
            self.densidad = []
            for (x,y) in self.n:
                self.lpq = []
                numvecino = len(self.vecinos[(x,y)])
                self.clustCoef2=0
                for t in range(0,numvecino-1):
                    self.clustCoef = 0
                    h = self.vecinos[(x,y)][t]
                    if (x,y) is not h:
                        for m in self.vecinos[h]:
                            if (x,y) is not m:
                                if m is not h:
                                    if h is not m:
                                        if h is not (x,y):
                                            if m is not (x,y):
                                                if m in self.vecinos[(x,y)]:
                                                    if (h,m) not in self.lpq:
                                                        self.lpq.append((h,m))
                                                    if (m,h) not in self.lpq:
                                                        self.lpq.append((m,h))
                                                        self.clustCoef = self.clustCoef + 1
                    self.clustCoef2 = self.clustCoef2 + self.clustCoef  
                dens = (self.clustCoef2)/(((numvecino)*(numvecino-1))/2)
                self.densidad.append(dens)
            c = 0
            for d in range(0,len(self.densidad)-1):
                c = c + self.densidad[d]
            self.DensidadPromedio = c/len(self.densidad)
            print(self.DensidadPromedio, file=crear)

    def graficar(self, plot):
        with open("grafo.plot","w") as archivo:
             print("set term eps", file=archivo)
             print("set output 'grafo4.eps'", file=archivo)
             print("set xrange [-.1:1.1]", file=archivo)
             print("set yrange [-.1:1.1]", file=archivo)
             print("set pointsize .7", file=archivo)
             print("set size square", file=archivo)
             print("set key off", file=archivo)
             num = 0
             for key in self.aristas:
                 x1 = key[0][0] 
                 y1 = key[0][1] 
                 x2 = key[1][0] 
                 y2 = key[1][1]
                 p = self.aristas[key]
                 if p > k:
                     print("set arrow {:d} from {:f},{:f} to {:f}, {:f} nohead lw 1 lc 1".format(num+1,x1,y1,x2,y2),file=archivo)
                 else:
                     print("set arrow {:d} from {:f},{:f} to {:f}, {:f} nohead lw 1".format(num+1,x1,y1,x2,y2),file=archivo)
                 num+=1
             print("plot 'NodosWarshall.dat' using 1:2 with points pt 7 lc 6", file=archivo)
             print("show arrow", file=archivo)
             print("quit()",file=archivo)  

    def FloydWarshall(self):
        self.d = {}
        for (x,y) in self.n:
            self.d[((x,y),(x,y))] = 0 
            for u in self.vecinos[(x,y)]: 
                self.d[((x,y),u)] = self.aristas[((x,y),u)]
        for intermedio in self.n:
            for desde in self.n:
                for hasta in self.n:
                    di = None
                    if (desde, intermedio) in self.d:
                        di = self.d[(desde, intermedio)]
                    ih = None
                    if (intermedio, hasta) in self.d:
                        ih = self.d[(intermedio, hasta)]
                    if di is not None and ih is not None:
                        c = di + ih # largo del camino via "i"
                        if (desde, hasta) not in self.d or c < self.d[(desde, hasta)]:
                            self.d[(desde, hasta)] = c # mejora al camino actual
        return self.d

i = 340
Tk = i/2
k = ceil(i/4)
k = 1
p = 0.1
Grafo = Grafo()
Grafo.generar(i)
Grafo.conectar(k)
Grafo.conectaraleatorio(p)
Grafo.FloydWarshall()
Grafo.distancia()
Grafo.densidad()
Grafo.graficar("grafo.plot")


