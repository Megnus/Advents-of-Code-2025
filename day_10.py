import aoc
import ast
from collections import deque
import pulp

data = aoc.get_data(False)
data = [d.split(' ') for d in data]

extracted_data = []
button_data = []


def rearrange_data():
	for d in data:
		a, b, c = (d[0][1:-1], d[1:-1], d[-1])
		a = a[::-1][::].replace('#', '1').replace('.', '0')
		b = [x[1:-1].split(',') for x in b]
		b_bit = [[1 << int(y) for y in x] for x in b]
		n = 0
		for bit in a:
		    n = (n << 1) | int(bit)	
		c = [int(x) for x in c[1:-1].split(',')]
		extracted_data.append((n, b_bit, c))
		b_data = [[int(y) for y in x] for x in b]
		button_data.append((b_data, c))


def switch_lights(lights, switch):
	for s in switch:
		lights ^= s
	return lights


def bfs(tree, start, goal):
    visited = []
    queue = deque([[start, 0]])
    while True:
        node, count = queue.popleft()
        for neighbor in tree:
            node_x = switch_lights(node, neighbor)
            if node == goal:
                return count
            if node not in visited:
                queue.append([node_x, count + 1])


def part_1():
	count = 0
	for goal, switch, _ in extracted_data:
		counter = bfs(switch, 0, goal)
		count += counter

	return count


def part_2():
	D_structure = [[tuple(i for i, y in enumerate(X) if j in y) for j in range(len(Y))] for X, Y in button_data]
	sum_count = 0

	for j, p in enumerate(D_structure):
		d_buttons, d_results = button_data[j]
		prob = pulp.LpProblem("MinSum", pulp.LpMinimize)
		solver = pulp.PULP_CBC_CMD(msg=False)
		x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(len(d_buttons))]
		prob += pulp.lpSum(x)

		for l, n in enumerate(p):
			for i, m in enumerate(n):
				X = x[m] if i == 0 else X + x[m]
			prob += X == d_results[l]
		prob.solve(solver)
		sum_count += sum(int(v.value()) for v in x)

	return sum_count


rearrange_data()

print('part 1:', part_1())
print('part 2:', part_2())
