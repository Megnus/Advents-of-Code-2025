import aoc
from collections import deque

data = aoc.get_data(True)
data_dict = dict()


def rearrange_data():
	for d in data:
		d = d.replace(':', '')
		d = d.split(' ')
		data_dict[d[0]] = d[1:]


def bfs():
	count = 0
	dq = deque(['you'])
	visited = set()
	while dq:
		next_step = dq.popleft()
		visited.add(next_step)
		new_paths = data_dict[next_step]
		for np in new_paths:
			if np == 'out':
				count += 1
			else:
				dq.append(np)
	return count


def part_1():
    return bfs()


def part_2():
    return None


rearrange_data()

print('part 1:', part_1())
print('part 2:', part_2())
