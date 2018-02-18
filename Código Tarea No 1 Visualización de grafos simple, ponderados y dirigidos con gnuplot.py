from random import random
nodos = []
n = 100
p = 0.2
i = 1
with open("nodos.dat", 'w') as archivo:
    for nodo in range(n):
        x = random()
        y = random()
        nodos.append((x,y))
        print(x,y, file = archivo)

with open("nodos.plot", 'w') as archivo:
    print('set term png', file = archivo)
    print('set output "grafo.png"', file = archivo)
    print('set size square', file = archivo)
    print('set key off', file = archivo)
    print('set xrange [-0.1:1.1]', file = archivo)
    print('set yrange [-0.1:1.1]', file = archivo)
    for (x1, y1) in nodos:
        for (x2, y2) in nodos:
            if random() < p:
                print('set arrow',i, 'from', x1,',',y1,'to',x2,',',y2,'nohead', file = archivo)
                i += 1
    print('plot "nodos.dat" using 1:2 with points pt 7', file = archivo)
    print('quit()', file = archivo)
    
