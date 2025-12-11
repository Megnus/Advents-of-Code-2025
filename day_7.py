import aoc

data = aoc.get_data(True)

for d in data:
	print(d)

# S = [d.index('S') for d in data]
S = [(j, i) for i, d in enumerate(data) for j, x in enumerate(d) if x == 'S']
splits = [(j, i) for i, d in enumerate(data) for j, x in enumerate(d) if x == '^']
drops = set()

print(S)
print(splits)

count_splits = 0
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
	print(S, count_splits)
	print('----')


print(drops)

for i, d in enumerate(data):
	for j, e in enumerate(d):
		if (j, i) in drops:
			print('|', end='')
		else:
			print(e, end='')
	print()

print(count_splits)




def part_1():
    return None


def part_2():
    return None


print('part 1:', part_1())
print('part 2:', part_2())
