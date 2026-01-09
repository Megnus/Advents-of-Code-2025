import aoc
import itertools

data = aoc.get_data(True)
data = [tuple(int(i) for i in d.split(',')) for d in data]


def part_1():
    comb = list(itertools.combinations(data, 2))
    comb_dist = [(A, B, (abs(A[0] - B[0]) + 1) * (abs(A[1] - B[1]) + 1)) for A, B in comb]
    max_coordinate = max(comb_dist, key=lambda c: c[2])
    A, B, area = max_coordinate
    return area

min_x, min_y = min(x for x, _ in data), min(y for _, y in data)
max_x, max_y = max(x for x, _ in data), max(y for _, y in data)
all_x, all_y = [0] + [x for x, _ in data] + [max_x + min_x], [0] + [y for _, y in data] + [max_y + min_y]
x_ticks = sorted(set(all_x))
y_ticks = sorted(set(all_y))


def create_sub_rectangles(rectangle):
    A, B = rectangle
    x0, y0 = A
    xn, yn = B

    x_0, y_0 = min(x0, xn), min(y0, yn)
    x_n, y_n = max(x0, xn), max(y0, yn)
    x0, y0, xn, yn = (x_0, y_0, x_n, y_n)


    rec_ticks_x = [x for x in x_ticks if x0 <= x <= xn]
    rec_ticks_y = [y for y in y_ticks if y0 <= y <= yn]
    sub_rectangles = list()
    for y0, y1 in zip(rec_ticks_y[:-1], rec_ticks_y[1:]):
        for x0, x1 in zip(rec_ticks_x[:-1], rec_ticks_x[1:]):
            sub_rectangles.append([(x0, y0), (x1, y1)])
    result = sorted(sub_rectangles)
    return result if result else [A, B]


def rectangle_to_sides(rectangle):
    A, B = rectangle
    x0, y0 = A
    x1, y1 = B
    a = sorted(((x0, y0), (x1, y0)))
    b = sorted(((x1, y0), (x1, y1)))
    c = sorted(((x1, y1), (x0, y1)))
    d = sorted(((x0, y1), (x0, y0)))
    return  sorted((a, b, c, d))


def sides_to_rectangle(sides):
    all_x_in_sides = [x for side in sides for x, _ in side]
    all_y_in_sides = [y for side in sides for _, y in side]
    x_min, y_min = min(all_x_in_sides), min(all_y_in_sides)
    x_max, y_max = max(all_x_in_sides), max(all_y_in_sides)
    return [(x_min, y_min), (x_max, y_max)]


def get_fence():
    fence = [sorted([a, b]) for a, b in zip(data[:-1], data[1:])] + [sorted([data[-1], data[0]])]
    f_fence = []
    for f in fence:
        A, B = f
        x1, y1 = A
        x2, y2 = B
        if y1 == y2:
            r = [x for x in x_ticks if x1 <= x <= x2]
            r_zip = zip(r[:-1], r[1:])
            f_fence += [sorted([(a, y1), (b, y1)]) for a, b in r_zip]
        elif x1 == x2:
            r = [y for y in y_ticks if y1 <= y <= y2]
            r_zip = zip(r[:-1], r[1:])
            f_fence += [sorted([(x1, a), (x1, b)]) for a, b in r_zip]
    return f_fence


def get_neighbour_rectangles(rectangle, rectangle_list):
    neighbour_rectangles = [rect for rect in rectangle_list if rect != rectangle and
                            any(side in rectangle_to_sides(rectangle) for side in rectangle_to_sides(rect))]
    return neighbour_rectangles


def part_2():
    stack_rectangles = list()
    outside_rectangles = set()

    # All the sides in the fence.
    fence_side_list = get_fence()

    # The rectangle that covers all the sub rectangles.
    total_rectangle = [(min(x_ticks), min(y_ticks)), (max(x_ticks), max(y_ticks))]

    # All the sub rectangles
    total_rectangle_list = create_sub_rectangles(total_rectangle)

    # The stack of all the rectangles to search from... These will be filled.
    rectangle_search_stack = [total_rectangle_list[0]]

    # Explore the first rectangle.
    rectangle = rectangle_search_stack.pop(0)

    # Add this to rectangle on the outside.
    stack_rectangles.append(rectangle)

    all_fence_rect = [rect for rect in total_rectangle_list if
                      any(side in fence_side_list for side in rectangle_to_sides(rect))]

    # Rectangle to side
    rectangle_to_side_dict = {tuple(rect): rectangle_to_sides(rect) for rect in total_rectangle_list}

    # Side to rectangle
    side_to_rectangle_dict = dict()
    for rect in total_rectangle_list:
        for side in rectangle_to_sides(rect):
            side_to_rectangle_dict[tuple(side)] = side_to_rectangle_dict.get(tuple(side), []) + [rect]

    # Rectangle to rectangle
    rectangle_to_rectangle_dict = dict()
    for rect, sides in rectangle_to_side_dict.items():
        for side in sides:
            rectangle_to_rectangle_dict[tuple(rect)] = (
                    rectangle_to_rectangle_dict.get(tuple(rect), []) + side_to_rectangle_dict.get(tuple(side), []))

    for k, v in rectangle_to_rectangle_dict.items():
        rectangle_to_rectangle_dict[k] = [rect for rect in v if rect != list(k)]

    while stack_rectangles:
        rectangle = stack_rectangles.pop(0)
        if tuple(rectangle) in outside_rectangles:
            continue
        outside_rectangles.add(tuple(rectangle))
        if rectangle in all_fence_rect:
            fence_sides_in_rectangle = [side for side in rectangle_to_side_dict[tuple(rectangle)] if side in fence_side_list]
            all_neighbours = rectangle_to_rectangle_dict[tuple(rectangle)]
            all_neighbours_without_fence_side = [rect for rect in all_neighbours if not any(side in fence_sides_in_rectangle for side in rectangle_to_side_dict[tuple(rect)])]
        else:
            all_neighbours_without_fence_side = rectangle_to_rectangle_dict[tuple(rectangle)]
        stack_rectangles += all_neighbours_without_fence_side

    outside_rectangles = set(tuple(r) for r in outside_rectangles)
    comb = list(itertools.combinations(data, 2))
    comb_dist = [(A, B, (abs(A[0] - B[0]) + 1) * (abs(A[1] - B[1]) + 1)) for A, B in comb]
    sorted_comb_dist = sorted(comb_dist, key=lambda c: c[2], reverse=True)

    max_area = 0
    for A, B, area in sorted_comb_dist:
        if not any(tuple(sub_rect) in outside_rectangles for sub_rect in create_sub_rectangles(sorted([A, B]))):
            max_area = area
            break

    return max_area


print('part 1:', part_1())
print('part 2:', part_2())
