import sys, math, random
t = [-0.56047565, -0.23017749, 1.55870831, 0.07050839, 0.12928774, 1.71506499,
0.46091621, -1.26506123, -0.68685285, -0.44566197, 1.22408180, 0.35981383,
0.40077145, 0.11068272, -0.55584113, 1.78691314, 0.49785048, -1.96661716,
0.70135590, -0.47279141, -1.06782371, -0.21797491, -1.02600445, -0.72889123]

n = len(t)
for i in range(n):
	t[i] = round(t[i], 1)

def stem(x):
	x = sorted(x)
	n = len(x)
	mini = int(min(x))
	maxi = int(max(x))
	l = maxi - mini + 2
	c = [[] for i in range(l)]
	zn1 = mini
	y = 0
	for i in range(l):
		
		
		for j in range(n):
			if x[j] <= (mini +i) and x[j] > ((mini + i) -1):
				c[i].append(int(abs(x[j] -zn1)*10))
		if zn1 == 0 and y ==0:
			y += 1
			
		else: zn1 += 1
	zn2 = mini
	y = 0	
	for i in range(l):
		if zn2 == 0 and y ==0:
			print("-{0}  | ".format(zn2), end = "")
		
		else: print("{0}  | ".format(zn2), end = "")
		g = len(c[i])
		
		for j in range(g):
			print("{0}".format(c[i][j]), end = "")
		
		print("\n")
		
		if zn2 == 0 and y ==0:
			y += 1
			
		else: zn2 += 1
		
stem(t)
			
		
			
		
	
	
