import math, sys
x = [0,0,0,1,1,0,2,2,1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
f = ["mezczyzna", "kobieta","ufo"]
k = len(f)
def table(x,k):
	n = len(x)
	p = [0]*k
	for i in range(n):
		p[x[i]] += 1
	return p
t = table(x,k)
color = ["r", "b", "g", "y"]

def barplot(t,f):
	import matplotlib.pyplot as plt
	import matplotlib.patches as patches
	fig = plt.figure()
	ax = fig.add_subplot(111)
	
	ax.set_xlim([0, int((max(t) + min(t))/1.2)])
	ax.set_ylim([0.0, max(t)*1.1])
	w = int((max(t) + min(t))/1.2)
	for i in range(k):
		xy = [[w/30+ i* 1/3*w, 0],
			  [(9/30 * w)+ i* 1/3*w, 0],
			  [(9/30 * w)+ i* 1/3*w, t[i]],
			  [w/30+ i* 1/3*w, t[i]]
		]
		ax.add_patch(patches.Polygon(
				xy, facecolor=color[i]
		))
		ax.text(w*4/30+ i* 1/3*w,t[i],"{0}".format(f[i]),horizontalalignment="center", verticalalignment="bottom")
		
	
	
	
	fig.savefig("output.png", dpi=90)

barplot(t,f)
	
	
	
