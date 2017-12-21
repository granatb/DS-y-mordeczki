import sys, math, random
t = [0,0,0,1,1,0,1,2,0,2]	
def table(x, k):
	n = len(x)
	c = [0]*k
	for i in range(n):
		c[x[i]] += 1
	return c
	
f =["mezczyzna", "kobieta", "ufo"]
l = len(f)
t = table(t, l)
print(t)
def stosunek(l,t):
		y = [0] * l
		suma = 0
		for j in range(l):
			suma += t[j]	
			
		for i in range(l):
			y[i] = t[i]/suma
		
		return y
			
def okrag(n, z):
	r = []
	def eng(j):
		it = 0
		if j == 0:
			return 0
		else:
			for i in range(j):
				it += stosunek(l,t)[i]
			
		return it
	dl = len(z)

	for k in range(dl):
		d = [0]*int(n*z[k])
		b = [0]*int(n*z[k])
		g = int(n*z[k])
		wu = eng(k)*n
		print(wu)
		
		for i in range(g):
			d[i] = 5*math.cos((wu + i)*(math.pi*2/n))
		for i in range(g):
			b[i] = 5*math.sin((wu + i)*(math.pi*2/n))
		li = [[0]*2 for i in range(g+1)]
	
		for i in range(1, g):
			li[i][0] = d[i]
			li[i][1] = b[i]
		r.append(li)
	
	
	
	return r
	

l = len(f)		
color = ["r", "b", "y", "g"]
def piechart(t, f):
	
	
	import matplotlib.pyplot as plt
	import matplotlib.patches as patches
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_xlim([0, 10])
	ax.set_ylim([0, 10])
	l = len(f)
	for i in range(l):
		
	
		xy = okrag(2000, stosunek(l,t))[i]
		ax.add_patch(patches.Polygon(
			xy, facecolor=color[i]
		))
		ax.text(1.5*okrag(2000,stosunek(l,t))[i][100][0],1.5*okrag(2000,stosunek(l,t))[i][100][1],"{0}".format(f[i]), horizontalalignment="center", verticalalignment="bottom")
	
	ax.axis("off")
	ax.axis("equal")
	
	fig.savefig("output2.png", dpi = 90)


piechart(t, f)
















































	
	
