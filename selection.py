import random
import copy

def selection(t):
	n=len(t)
	i=0
	j=0
	k=0
	while i<n-1:
		k=i
		j=i+1
		while j<n:
			if t[k]> t[j]: 
				k=j
			j+=1
		t[i], t[k] = t[k], t[i]
		i+=1
	return t

def selection_p(t):
	n=len(t)
	i=0
	u=[0]*n
	while i<n:
		u[i]=i
		i+=1	
	i=0
	j=0
	k=0
	while i<n-1:
		k=i
		j=i+1
		while j<n:
			if t[u[k]]> t[u[j]]: 
				k=j
			j+=1
		u[i], u[k] = u[k], u[i]
		i+=1
	return u
		





i=0
t=[0]*10
while i<10:
	t[i]=random.randint(0,100)
	i+=1
print(t)
print(selection_p(t)) 