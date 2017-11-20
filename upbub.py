def bubble_sort(t):
	n = len(t)
	o = n - 1 
	for i in range(0, n-1):
		if (o == n - 1 or n - i) and i >= 1:
			o = n - 1 - i
		for j in range(0, o):
			if not ( t[j] <= t[j+1]):
				t[j], t[j+1] = t[j+1], t[j]
				o = j + 1
			else: o = 0
	return t
t = [0] * 10000
def tworzenietablicyzpomyslumacka(t):
	for i in range(0, len(t)):
		t[i] = i
	
	return t
d = tworzenietablicyzpomyslumacka(t)
print(bubble_sort(d))
