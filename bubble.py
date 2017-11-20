import random
import copy
import math
def bubble(t):
	n=len(t)
	i=0
	j=0
	while i<n-1:
		j=0
		while j<n-i-1:
			if t[j]>t[j+1]:
				t[j], t[j+1]=t[j+1], t[j]
				
			j+=1
		#print(math.ceil(i/n*10000)/100, "%") #to tylko licznik postępu		
		i+=1
	return t

def bubble_wartownik(t):
	n=len(t)
	i=0
	j=0
	wartownik_s=n-1
	wartownik=n-1
	while i<n-1:
		if wartownik==0: break		
		j=0
		wartownik_s=wartownik
		wartownik=0
		while j<wartownik_s:
			if t[j]>t[j+1]:
				t[j], t[j+1]=t[j+1], t[j]
				wartownik=j
			j+=1
		#print(math.ceil(i/n*10000)/100, "%")		
		i+=1
	return t


def bubble_p(t):
	n=len(t)
	u=[0]*n
	i=0
	while i<n:
		u[i]=i
		i+=1
	i=0
	j=0
	w=0
	while i<n-1:
		j=0
		while j<n-i-1:
			if t[u[j]]>t[u[j+1]]:
				u[j], u[j+1]=u[j+1], u[j]
			j+=1		
		i+=1
	return u

#ZAUWAZYŁEM SIE WYPPIERDALA SIE DLA WIKESZYCH TABLIC ALE NIE CHCE MI SIE NAPRAWIAC
def szukaj_i(p, i, j):
	m=len(p)
	
	while j<m:
		if p[j]==i: return j
		j+=1
	


def permute(p, t):
	n=len(t)
	i=0	
	while i<n:
		
		t[i], t[p[i]]=t[p[i]], t[i]
		print("		", i, "		", p)		
		print(szukaj_i(p, i, i))
		p[szukaj_i(p, i, i)]=szukaj_i(t, t[p[i]], 0)
		i+=1
	return t 
	



random.seed(73)
i=0
#p=[7, 0, 2, 6, 1, 5, 8, 4, 9, 3]
#t=[9, 3, 5, 0, 1, 23, 2, 7, 98, 6]
t=[0]*20
n=len(t)
while i<20:
	t[i]=random.randint(0,100)	
	i+=1
print(t)
print(bubble_p(t))
print(permute(bubble_p(t), t))
#print(p)