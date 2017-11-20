def bubble(l):
	n = len(l)
	t = 0
	v = 0
	x = [i for i in range(n)]
	for j in range(n-1):
		for i in range(n - j - 1):
			v += 1
			if not (l[i] <= l[i+1]):
				t += 1
				l[i], l[i+1] = l[i+1], l[i]
				x[i], x[i+1] = x[i+1], x[i]
				
	for i in range(n):
		x[i] = n - 1 - x[i]
	return l, x
				
import random
random.seed(1)
l = [random.randint(0, 4) for i in range(4)]
print(l)
print(bubble(l))

def insert(l):
	n = len(l)
	t = 0
	v = 0
	x = [i for i in range(n)]
	for i in range(n-1):
		for j in range(i+1):
			v += 1
			if  not (l[i+1-j] >= l[i-j]):
				l[i+1-j], l[i-j] = l[i-j], l[i+1-j]
				x[i+1-j], x[i-j] = x[i-j], x[i+1-j]
				t += 1
			else: break
				
	for i in range(n):
		x[i] = n - 1 - x[i]
	return l, x
	
random.seed(1)
l = [random.randint(0, 4) for i in range(4)]
print(insert(l))

def selection(l):
	n = len(l)
	v = 0
	t = 0
	x = [i for i in range(n)]
	for i in range(n-1):
		k = i
		for j in range(i+1, n):
			v += 1
			if l[j] < l[i]:
				i = j
				t += 1
		l[i], l[k] = l[k], l[i]
		x[i], x[k] = x[k], x[i]
				
	for i in range(n):
		x[i] = n - 1 - x[i]
	return l, x
	

	

random.seed(1)
l = [random.randint(0, 4) for i in range(4)]
print(selection(l))


def permute(t, p):
	n = len(t)
	for i in range(n):
		t[i], t[p[i]] = t[p[i]], t[i]
		for j in range(n):
			if i == p[j]:
				k = j
				break
		p[i], p[k] = p[k], p[i]
				
	return t
	
h = [3, 0, 4, 1, 2]
g = [1, 3, 4, 0, 2]

print(permute(h, g))
		
def binsearch(t, v):
	n = len(t)
	c = n//2
	a = 0
	b = n-1
	while a <= b:
		if t[c] == v: 
			return c
			break
		elif t[c] < v:
			a = c +1
		else: b = c -1
		c = (a+b)//2
	
t = [1, 2, 3, 4, 5]
v = 1
print(binsearch(t, v))















































	
