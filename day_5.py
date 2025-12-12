import aoc

data = aoc.get_data(True)
fresh = []
ingredients = []
index = 0
d = data[0]

while d != '':
	fresh.append([int(i) for i in d.split('-')])
	index += 1
	d = data[index]

while index < len(data) - 1:
	index += 1
	ingredients.append(int(data[index]))


def part_1():
	fresh_ingredients = []
	for e in ingredients:
		for a, b in fresh:
			if a <= e <= b:
				fresh_ingredients.append(e)
				break
	return len(fresh_ingredients)


def part_2():
	fresh_ingredients = []
	index_to_remove = []
	i = 0
	while i < len(fresh):
		a, b = fresh[i]
		j = 0
		while j < len(fresh):
			if j != i:
				c, d = fresh[j]
				if c <= b <= d:
					if not c <= a <= d:							
						fresh[j] = [a, d]
					fresh.pop(i)
					i = 0
					break
			j += 1
		i += 1			
	return sum(b - a + 1 for a, b in fresh)


print('part 1:', part_1())
print('part 2:', part_2())
