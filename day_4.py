import aoc

data = aoc.get_data(True)
data = [list(row) for row in data]
dxdy = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))


def part_1():
    result = set()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] != '@':
                continue
            c = 0
            for dx, dy in dxdy:
                nx, ny = (x + dx, y + dy)
                if 0 <= nx < len(data[0]) and 0 <= ny < len(data):
                    if data[ny][nx] == '@':
                        c += 1
            if c < 4:
                result.add((x, y))

    return len(result)


def part_2():
    tot_count = -1
    result = set()

    while tot_count < len(result):
        tot_count = len(result)
        for y in range(len(data)):
            for x in range(len(data[0])):
                if data[y][x] != '@':
                    continue
                c = 0
                for dx, dy in dxdy:
                    nx, ny = (x + dx, y + dy)
                    if 0 <= nx < len(data[0]) and 0 <= ny < len(data):
                        if data[ny][nx] == '@':
                            c += 1
                if c < 4:
                    result.add((x, y))

        for y in range(len(data)):
            for x in range(len(data[0])):
                if (x, y) in result:
                    data[y][x] = 'x'

    return tot_count


print('part 1:', part_1())
print('part 2:', part_2())
