from random import random, randint, choice, sample
from math import sqrt



class grafocontra:

	def __init__(self):
		self.aristas = dict()
		self.A = []
		self.pesos = []
		self.nodos = []
		self.aux = []
		self.n = None

	def puntos (self, num):
		self.n = num
		self.nodos.append((-.2, 0.4, 0))
		self.aux.append((0))
		for i in range(1, self.n - 1):
			self.nodos.append((random(), random(), i))
			self.aux.append((i))
		self.nodos.append((1.2, 0.4, self.n -1))
		self.aux.append((self.n -1))

	def conectar (self, prob):
		for (x1, y1, u) in self.nodos:
			for(x2, y2, v) in self.nodos:
				if random() < prob:
					self.aristas[(u,v)] = self.aristas[(v, u)] = int(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * 10)
					self.A.append((x1, y1, x2, y2, u, v))
					self.pesos.append((sqrt((x2 - x1) ** 2 + (y2 - y1 )** 2)*10, (x1+x2)/2, (y1+y2)/2))

	def contraccion(self):
		while len(self.aux) > 2:
			w = choice(self.aux) 
			z = choice(self.aux) 
			if w is not z:
				if w is not self.nodos[0][2] and w is not self.nodos[len(self.nodos) - 1][2]:
					if w in self.aux:
						self.aux.remove(w)
						print (self.aux)
						print (w, z)
						for i in range(0, len(self.nodos) - 1):
							if w is self.nodos[i][2]:
								self.nodos.pop(i)
								print(self.nodos)	

		print(self.nodos)
					



	def imprimir(self, num):
		with open("grafo"+str(num)+".dat", 'w') as salida:
			for n in range(self.n):
				print(self.nodos[n][0], self.nodos[n][1], self.nodos[n][2], file = salida)


	def imprimir2(self, num):
		with open("grafo"+str(num)+".dat", 'w') as salida:
			for n in range(len(self.nodos)):
				print(self.nodos[n][0], self.nodos[n][1], self.nodos[n][2], file = salida)



	def grafica (self,num,  eps = True):
		with open("nodos"+str(num)+".plot", 'w') as salida: 
			if eps:
				print("set term postscript color eps", file = salida)
				print('set output "nodos'+str(num)+'.eps"', file = salida)
			else:
				print('set term png', file = salida)
				print('set output "nodos.png"', file = salida)
			print('set size square', file = salida)
			print('set key off', file = salida)
			print ('set xrange [-.5:1.5]', file = salida)
			print ('set yrange [-.1:1.1]', file = salida)
			for n in range(len(self.nodos)):
				print('set label', " ' " , self.nodos[n][2], "   ' ", 'at', self.nodos[n][0], ",", self.nodos[n][1],  file = salida )
			
			id = 1
			for i in range(len(self.A)):
				print('set arrow', id, 'from', self.A[i][0], ',', self.A[i][1], 'to', self.A[i][2], ',', self.A[i][3], 'nohead filled lw 1', file = salida)
				#print('set label', " ' ", int(self.pesos[i][0]), " ' ", 'at', self.pesos[i][1], ',', self.pesos[i][2], file = salida)
				id += 1
			print('plot "grafo'+str(num)+'.dat" using 1:2:3 with points pt 7 lc var ps 2 ', file = salida)
			print('quit()', file =  salida)


G = Grafo()
G.puntos(6)
G.imprimir(1)
G.conectar(0.1)
G.contraccion()
G.grafica(1)
G.imprimir2(2)
G.grafica(2)
