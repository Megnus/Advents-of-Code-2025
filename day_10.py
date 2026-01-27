import aoc
import ast
from collections import deque  # Import deque for efficient queue operations
import pulp

data = aoc.get_data(True)
data = [d.split(' ') for d in data]
# print(data)
# exit()

extracted_data = []
button_data = []
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


# Define the BFS function
def bfs(tree, start, goal):
    visited = []  # List to keep track of visited nodes
    queue = deque([[start, 0]])  # Initialize the queue with the starting node
    while True:  # While there are still nodes to process
        node, count = queue.popleft()  # Dequeue a node from the front of the queue
        # Enqueue all unvisited neighbors (children) of the current node
        for neighbor in tree:
            node_x = switch_lights(node, neighbor)
            if node == goal:
                return count
            if node not in visited:
                queue.append([node_x, count + 1])  # Add unvisited neighbors to the queue


def part_1():
	count = 0
	for goal, switch, _ in extracted_data:
		counter = bfs(switch, 0, goal)
		count += counter

	return count


# print(extracted_data)
# print(button_data)

# # Problem
# prob = pulp.LpProblem("MinSum", pulp.LpMinimize)
# solver = pulp.PULP_CBC_CMD(msg=False)

# # Variables (positive integers)
# x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(6)]

# # Objective
# prob += pulp.lpSum(x)

# Constraints
# prob += x[0] + x[1] + x[2] == 10
# prob += 2*x[0] + x[1] == 6


# X, Y = ([[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]], [3, 5, 4, 7])

# # for i, D in enumerate(button_data):
# # 	X, Y = D
# # for X, Y in button_data:
# print(button_data)
# print('+'*10)

sum_count = 0

x_poses = []
x_poses = [[tuple(i for i, y in enumerate(X) if j in y) for j in range(len(Y))] for X, Y in button_data]
	# x_pos = [i for i, y in enumerate(X) if j in y]
	# x_poses.append(x_pos)

for j, p in enumerate(x_poses):
	bd_butt, bd_res = button_data[j]

	prob = pulp.LpProblem("MinSum", pulp.LpMinimize)
	solver = pulp.PULP_CBC_CMD(msg=False)

	# print(button_data[j][0], '--------------*****')
	# Variables (positive integers)
	x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(len(bd_butt))]

	# Objective
	prob += pulp.lpSum(x)
	for l, n in enumerate(p):
		# print(n, '/')
		for i, m in enumerate(n):
			# print(m, '*')
			if i == 0:
				# print(n)
				ty = x[m]
				
			else:
				ty += x[m]
		prob += ty == bd_res[l]
		# print(bd_res[l])
		# print(10*'-')
		#break
	prob.solve(solver)

	# print([v.value() for v in x])
	# print("Sum:", sum(v.value() for v in x))
	# print(n)
	sum_count += sum(v.value() for v in x)

print(sum_count)
exit()

"""
# prob += x[4] + x[5] == 3
n, m = (4, 5)
ty = x[n]
ty += x[m]
prob += ty == 3
prob == 3
"""
# prob += x[1] + x[5] == 5
# prob += x[2] + x[3] + x[4] == 4
# prob += x[0] + x[1] + x[3] == 7


# prob += x[0] + x[2] + x[3] == 7
# prob += x[3] + x[4] == 5
# prob += x[0] + x[1] + x[3] + x[4] == 12
# prob += x[0] + x[1] + x[4] == 7
# prob += x[0] + x[2] + x[4] == 2

# prob +=  x[0] + x[1] + x[2] == 10
# prob +=  x[0] + x[2] + x[3] == 11
# prob +=  x[0] + x[2] + x[3] == 11
# prob +=  x[0] + x[1] == 5
# prob +=  x[0] + x[1] + x[2] == 10
# prob +=  x[2]== 5

# Vilka index har 0 i sig --> 



# Solve
# prob.solve(solver)

# print([v.value() for v in x])
# print("Sum:", sum(v.value() for v in x))






def part_2():
    return None


print('part 1:', part_1())
print('part 2:', part_2())
