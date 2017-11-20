import random
def insertion(t):
	n=len(t)	
	i=1
	j=0
	while i<n:
		j=i
		while j>0 and t[j-1]>t[j]:
			t[j-1], t[j] = t[j], t[j-1]
			j-=1
		i+=1
	return t

def insertion_p(t):
	n=len(t)	
	p=[0]*n	
	j=0
	while j<n:
		p[j]=j
		j+=1	
	i=1
	j=0
	while i<n:
		j=i
		while j>0 and t[p[j-1]]>t[p[j]]:
			p[j-1], p[j] = p[j], p[j-1]
			j-=1
		i+=1
	return p

i=0
t=[0]*10
while i<10:
	t[i]=random.randint(0,100)
	i+=1
print(t)
print(insertion_p(t)) 