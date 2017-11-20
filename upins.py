import random
def insertion_sort(t):
	n = len(t)
	for i in range(1, n):	
		k = i
		l = 0
		p = k
		while k > 0:
			if not (t[p] >= t[k - 1]):
				l += 1
				
				
				
			else:
				if not (k - 1 == p - 1):
					g = t[p]
					for d in range(0, l):
						t[k + l -d] = t[k-1 +l -d]
					t[k] = g
				break
			k -= 1
			if k == 0:
				g = t[p]
				for d in range(0, l):
					t[k + l -d] = t[k-1 +l -d]
				t[k] = g
				
	return t

t = [0] * 10
def tworzenietablicyzpomyslumacka(t):
	for i in range(0, len(t)):
		t[i] = i
	
	return t
d = tworzenietablicyzpomyslumacka(t)
print(insertion_sort(d))

def schuffle(t):
	n = len(t)
	for i in range(n-1,0,-1):
		j = random.randint(0, i)
		t[i], t[j] = t[j], t[i]
	return t
v = schuffle(tworzenietablicyzpomyslumacka(t))
print(insertion_sort(v))