import aoc
import math

data = aoc.get_data(True)
nd = []
ad = []

for d in data:
	if '+' not in d:
		nd.append([int(x) for x in d.split(' ') if x.isnumeric()])
	elif '+' in d:
		ad = [x for x in d.split(' ') if x != '']


def part_1():
    T = [[nd[j][i] for j in range(len(nd))] for i in range(len(nd[0]))]
    col_sum = []
    for i, t in enumerate(T):
    	if ad[i] == '+':
    		col_sum.append(sum(t))
    	elif ad[i] == '*':
    		col_sum.append(math.prod(t))
    	else:
    		print('error')
    return sum(col_sum)



def part_2():
	new_data = [list(d) for d in data]
	T = [[new_data[j][i] for j in range(len(new_data))] for i in range(len(new_data[0]))]
	q = [i for i, t in enumerate(T) if all(p == ' ' for p in t)]
	q.append(len(new_data[0]))
	m = 0

	my_list = []
	daa = [list(d) for d in data]
	for d in data:
		m = 0
		ny_list = []
		for n in q:
			ny_list.append(list(d[m:n].replace(' ', '_')[::-1]))
			m = n + 1
		my_list.append(ny_list)


	for i in range(len(my_list)):
		for j in range(len(my_list[i])):
			e = my_list[i][j]

	yy = []
	ff = []
	for j in range(len(my_list[0])):
		for k in range(len(my_list[0][j])):
			xx = []
			for i in range(len(my_list)):
				try:
					e = my_list[i][j][k]
					if e == '+' or e == '*':
						xx.append(e)
						break
					if e != '_':
						xx.append(e)
					
				except:
					pass

			if '*' in xx or '+' in xx:
				ff.append(int(''.join(xx[:-1])))
				ff.append(xx[-1])
				yy.append(ff)
				ff = []
			elif xx:
				ff.append(int(''.join(xx)))

	tot = []
	for b in yy:
		if b[-1] == '+':
			tot.append(sum(b[:-1]))
		elif b[-1] == '*':
			tot.append(math.prod(b[:-1]))
			
	return sum(tot)


print('part 1:', part_1())
print('part 2:', part_2())
