"""
zadanie_6_0
"""
import csv
tips = []
f = open("tips.csv", "r") # r=do odczytu
for row in csv.reader(f):
	tips.append(row)
f.close()
n = len(tips)
m = len(tips[0])
total_bill = [0 for i in range(n)]
tip = [0 for i in range(n)]
sex = [0 for i in range(n)]
smoker = [0 for i in range(n)]
day = [0 for i in range(n)]
time = [0 for i in range(n)]
size = [0 for i in range(n)]
for i in range(n):
	total_bill[i] = float(tips[i][0])
	tip[i] = float(tips[i][1])
	sex[i] = tips[i][2]
	smoker[i] = tips[i][3]
	day[i] = tips[i][4]
	time[i] = tips[i][5]
	size[i] = tips[i][6]
def unique(t):
	k = len(t)
	tempdict = [None for i in range(k)]
	sortedt = sorted(t)
	miejsce = 1
	zlicz = 0
	tempdict[0] = sortedt[0]
	for i in range (1, k):
		if sortedt[i] != sortedt[i-1]:
			tempdict[miejsce] = sortedt[i]
			miejsce += 1
	i = 0
	while tempdict[i] != None:
		zlicz += 1
		i += 1		
	t_dict = [0 for i in range(zlicz)]
	for i in range(zlicz):
		t_dict[i] = tempdict[i]
	return t_dict
print(sex)
print(unique(sex))
def encode(x, t):
	n = len(t)
	m = len(x)
	sortedx = sorted(x)
	temp_list = [0 for i in range(n)]
	for i in range(n):
		for j in range(m):
			if x[j] == t[i]:
				x[j] = i
	return x
print(encode(sex, unique(sex)))
def split(x, t):
	n = len((unique(t)))
	m = len(x)
	encodedt = encode(t, unique(t))
	split = [[] for i in range(n)]
	for i in range(n):
		for j in range(m):	
			if encodedt[j] == i:
				split[i].append(x[j])
	return split
print(unique(day))
print(split(size, day))		 
		
