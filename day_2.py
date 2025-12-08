import aoc

data = aoc.get_data(True)
data = [d.split('-') for d in data[0].split(',')]

def part_1():
    count = 0
    for d in data:
        for i in range(int(d[0]), int(d[1]) + 1):
            i_str = str(i)
            i_len = len(i_str)
            a = i_str[:i_len // 2]
            b = i_str[i_len // 2:]
            if a == b:
                count += i
    return count

def split_into_chunks(s, n):
    try:
        return [s[i:i+n] for i in range(0, len(s), n)]
    except:
        return []

def part_2():
    count = 0
    for d in data:
        for i in range(int(d[0]), int(d[1]) + 1):
            i_str = str(i)
            i_len = len(i_str)
            for j in range(i_len):
                result = split_into_chunks(i_str, j)
                all_equal = len(set(result)) == 1
                if all_equal:
                    count += 1
                    break


    return count

print('part 1:', part_1())
print('part 2:', part_2())
