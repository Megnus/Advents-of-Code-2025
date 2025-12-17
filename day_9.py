import aoc
import itertools

data = aoc.get_data(True)
data = [tuple(int(i) for i in d.split(',')) for d in data]


def part_1():
    comb = list(itertools.combinations(data, 2))
    #print(comb)
    comb_dist = [(A, B, (abs(A[0] - B[0]) + 1) * (abs(A[1] - B[1]) + 1)) for A, B in comb]
    """
    print(comb_dist)
    for cd in comb_dist:
        print(cd)
    """
    max_coordinate = max(comb_dist, key=lambda c: c[2])
    A, B, area = max_coordinate
    return area


def part_2():
    return None


print('part 1:', part_1())
print('part 2:', part_2())
