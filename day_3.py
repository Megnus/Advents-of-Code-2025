import aoc

data = aoc.get_data(True)


def part_1():
    sum_tot = 0
    for d in data:
        max_tot = 0
        for i, x in enumerate(d):
            for j in range(i + 1, len(d)):
                tot = int(x + d[j])
                if tot > max_tot:
                    max_tot = tot
        sum_tot += max_tot


    return sum_tot

def max_to_have_left(str_num, left):
    str_len = len(str_num) + 1
    s = str_num[:str_len - left]
    return s

def the_largest_index(str_num, left):
    ar = max_to_have_left(str_num, left)
    i, m = max(enumerate(list(ar)), key=lambda x: x[1])
    return i, m, str_num[i + 1:]

def recursive_num(str_num):
    max_num = ''
    for i in range(12, 0, -1):
        index, m, str_num = the_largest_index(str_num, i)
        max_num += str(m)
    return int(max_num)

def part_2():
    sum_tot = 0
    for d in data:
        sum_tot += recursive_num(d)
    return sum_tot

print('part 1:', part_1())
print('part 2:', part_2())
