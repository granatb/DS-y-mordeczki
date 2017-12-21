#1
def table(x,k):
	"""zwraca tabelę liczności"""
	l=[0]*k
	n=len(x)
	for i in range (n):
		l[x[i]]+=1
	return l

#2
def piechart(t,f):
	"""zwraca wykres kołowy na podstawie tabelki liczności i wektora etykiet"""
	def average(l,i,wsp):
		"""dla 3-wymiarowej listy l zwraca średnią 2. wymiaru z i z 1. wymiaru i wsp z 3. wymiaru """
		suma=0
		n=len(l[i])
		for j in range (n):
			suma+=l[i][j][wsp]
		avg=suma/n
		return avg
	import matplotlib.pyplot as plt
	import matplotlib.patches as patches
	fig = plt.figure()
	ax = fig.add_subplot(111)
	
	# ustal zakresy na osiach:
	ax.set_xlim([0.0, 2.0]) # zakres wartości na osi OX
	ax.set_ylim([0.0, 2.0]) # zakres wartości na osi OY

	# przykładowy jasnoszary wielokąt:
	import math
	xy=[[0]*2 for i in range (720000)]
	
	#lista koła
	for i in range (720000):
		xy[i][0]=1+math.cos((i/360000)*math.pi)
		xy[i][1]=1+math.sin((i/360000)*math.pi)
	
	SUMAin=sum(t)
	o=len(t)
	Alpha=[]
	licznik=0 #do zliczania przypisań punktów z okręgu
	for i in range(o):
		frac=int((t[i]/SUMAin)*720000)
		Alpha.append([])
		for j in range(licznik,frac+licznik): #przypisywanie punktów z okręgu
			Alpha[i].append(xy[j])
			licznik+=1
		Alpha[i].append([1,1]) #dodawanie środka okręgu
		colour=["g","r","c","m","y","k"] #tablica kolorów
		ax.add_patch(patches.Polygon(
		Alpha[i], facecolor=colour[i%6] #rysowanie kawałka pizzy
		))
		
		ax.text(average(Alpha,i,0), average(Alpha,i,1), f[i], horizontalalignment="center", verticalalignment="bottom")


	Blad=[0]*(SUMAin-licznik) #błąd=nieprzypisane punkty okręgu xy (co najwyżej len(t))
	for bl in range (licznik,SUMAin):
		Blad[bl-licznik]=xy[bl]
	Blad.append([1,1])
	ax.add_patch(patches.Polygon(
		Blad, facecolor="0"
	))

	ax.axis("off") # nie rysuj osi
	ax.axis("equal") # OX i OY proporcjonalne

	fig.savefig("piechart.png", dpi=90)

import random
x=[0,0,0,1,1,0,2,0,2,1]
f=["pies","kot","ser"]

piechart(table(x,3),f)

#3
def barplot(t,f):
	"""zwraca wykres kołowy na podstawie tabelki liczności i wektora etykiet"""
	import matplotlib.pyplot as plt
	import matplotlib.patches as patches
	fig = plt.figure()
	ax = fig.add_subplot(111)
	

	# przykładowy jasnoszary wielokąt:
	SUMAin=sum(t)
	o=len(t)
	colour=["g","r","c","m","y","k"]
	pasek=40*o

	# ustal zakresy na osiach:
	ax.set_xlim([0.0, 2+12.0*o]) # zakres wartości na osi OX
	ax.set_ylim([0.0, 2+pasek]) # zakres wartości na osi OY

	for i in range(o):
		proc=t[i]/SUMAin*pasek
		xy=[[12*i,0.0],[12*i,proc],[12*(i+1)-2,proc],[12*(i+1)-2,0.0]]
		ax.add_patch(patches.Polygon(
xy, facecolor=colour[i%6]
))
		ax.text(5+12*i, proc, f[i], horizontalalignment="center", verticalalignment="bottom")

	ax.axis("off") # nie rysuj osi
	ax.axis("equal") # OX i OY proporcjonalne

	fig.savefig("barplot.png", dpi=90)

import random
x=[0,0,0,1,1,2,1,0,1,1,2,3,3,3,3,3,3,3,3]
f=["xd","Xd","xD","XD"]

barplot(table(x,4),f)
