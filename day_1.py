import aoc

data = aoc.get_data(True)


def part_1():
    state = 50
    count = 0
    for d in data:
        rl, n = d[0], int(d[1:])
        state += n if rl == 'R' else -n
        count += 1 if state % 100 == 0 else 0
        state %= 100
    return count


def part_2():
    state = 50
    count = 0
    for d in data:
        rl, n = d[0], int(d[1:])
        for i in range(n):
            state += 1 if rl == 'R' else -1
            if state == -1:
                state = 99
            elif state == 100:
                state = 0
            if state == 0:
                count += 1
    return count 


print('part 1:', part_1())
print('part 2:', part_2())
