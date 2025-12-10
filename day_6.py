import aoc
import math

data = aoc.get_data(False)
nd = []
ad = []

# [d.split() for d in data]
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
    # print(col_sum)
    return sum(col_sum)



def part_2():
	new_data = [list(d) for d in data]
	print(data)
	T = [[new_data[j][i] for j in range(len(new_data))] for i in range(len(new_data[0]))]
	q = [i for i, t in enumerate(T) if all(p == ' ' for p in t)]
	q.append(len(new_data[0]))
	print(q)
	m = 0
	print('---')

	daa = [list(d) for d in data]
	for d in data:
		m = 0
		for n in q:
			print(d[m:n].replace(' ', '0')[::-1])
			m = n + 1
		print('---')

	# print(q)
	print(T)
	# for i in range(len(new_data)):
	# 	# for j in range(len(new_data[i]):
	# 	print(new_data[i])
	# 	print(all(new_data[i][j] == ' ' for j in new_data[i]))

	return None
	# do = [1 for d in data]
	# print(do)
	# T = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
	# print(T)

    # T = [[nd[j][i] for j in range(len(nd))] for i in range(len(nd[0]))]
    # T = [[str(s) for s in t] for t in T]
    
    # T = [[int(''.join([y[i] for y in t if i < len(y)])) for i in range(max(len(k) for k in t))] for t in T]



    # print(T)
    # exit()
    # col_sum = []
    # for i, t in enumerate(T):
    # 	if ad[i] == '+':
    # 		col_sum.append(sum(t))
    # 	elif ad[i] == '*':
    # 		col_sum.append(math.prod(t))
    # 	else:
    # 		print('error')
    # # print(col_sum)
    # return sum(col_sum)
    # return None


# print('part 1:', part_1())
print('part 2:', part_2())