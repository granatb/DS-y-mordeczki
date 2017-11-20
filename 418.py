import math
def cos(t):
	n = len(t)
	
	for i in range(n):
		if math.isnan(t[i]):
			k = i
			l = 0
			print(k)
			while math.isnan(t[k]):
				k += 1
				l += 1
				
				
			for z in range(l):
				t[i +z] = (t[i-1] + t[k]) / 2
	return t
	
t = [1, float('nan'), 3, float('nan'), float('nan'), 5]

print(cos(t))
		
