import aoc

data = aoc.get_data(True)
splits = [(j, i) for i, d in enumerate(data) for j, x in enumerate(d) if x == '^']


def part_1():
	S = [(j, i) for i, d in enumerate(data) for j, x in enumerate(d) if x == 'S']
	count_splits = 0
	drops = set()

	while S:
		next_s = S.pop()
		drops.add(next_s)
		sx, sy = next_s
		psx, psy = (sx, sy + 1)

		try:
			if data[psy][psx] == '^':
				split_bool = False
				if (psx - 1, psy) not in drops:
					S.append((psx - 1, psy))
					split_bool = True
				if (psx + 1, psy) not in drops:
					S.append((psx + 1, psy))
					split_bool = True
				if split_bool:
					count_splits += 1		
			else:
				S.append((psx, psy))
		except:
			pass


	for i, d in enumerate(data):
		for j, e in enumerate(d):
			if (j, i) in drops:
				print('|', end='')
			else:
				print(e, end='')
		print()

	return count_splits


def part_2():
	S = [[(j, i), 1] for i, d in enumerate(data) for j, x in enumerate(d) if x == 'S']
	height = len(data)
	min_height = 0
	count_splits = 1

	while S:
		min_height_temp = min([coord_sub[1] for coord_sub, _ in S])
		index = [i for i, x_coord_sub in enumerate(S) if x_coord_sub[0][1] == min_height_temp][0]
		next_s, n = S.pop(index)

		if min_height < min_height_temp:
			min_height = min_height_temp
			print('Progress: ', min_height, '/', height, 'branches: ', count_splits)

		sx, sy = next_s
		psx, psy = (sx, sy + 1)

		try:
			if data[psy][psx] == '^':
				S.append([(psx - 1, psy), n])
				S.append([(psx + 1, psy), n])	
				count_splits += n
			else:
				S.append([(psx, psy), n])
		except:
			pass

		P = []
		Q = set([coord_sub for coord_sub, _ in S])
		for coord in Q:
			SS = [n_sub for coord_sub, n_sub in S if coord == coord_sub]
			P.append([coord, sum(SS)])
		S = P

	return count_splits


print('part 1:', part_1())
print('part 2:', part_2())
