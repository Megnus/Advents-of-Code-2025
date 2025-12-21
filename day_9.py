import aoc
import itertools

data = aoc.get_data(False)
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

# --- Rectangle to subrectanglses ---
# Get all the x and y coordinates. x0, x1, x3...xn and y0, y1, y2, yn
# If big rect is (x0, y0), (xn, yn) 
#   --> (x0, y0), (x1, y1) * (x1, y0), (x2, y1) * (x2, y0), (x3, y1) ... (x[n-1], y0), (xn, y1)
#   --> (x0, y1), (x1, y2) * (x1, y1), (x2, y2) * (x2, y1), (x3, y2) ... (x[n-1], y1), (xn, y2)
#   --> (x0, y[n-1]), (x1, yn) * (x1, y[n-1]), (x2, yn) * (x2, y[n-1]), (x3, yn) ... (x[n-1], y[x-1]), (xn, yn)

def create_sub_rectangles(rectangle):
    A, B = rectangle
    x0, y0 = A
    xn, yn = B
    rec_ticks_x = [x for x in x_ticks if x0 <= x <= xn]
    rec_ticks_y = [y for y in y_ticks if y0 <= y <= yn]
    sub_rectangles = list()
    for y0, y1 in zip(rec_ticks_y[:-1], rec_ticks_y[1:]):
        for x0, x1 in zip(rec_ticks_x[:-1], rec_ticks_x[1:]):
            sub_rectangles.append([(x0, y0), (x1, y1)])
    return sorted(sub_rectangles)


# --- Two coordinate rectangle to side rectangle ---
# (x0, y0), (x1, y1) --> {{(x0, y0), (x1, y0)}, {(x1, y0), (x1, y1)}, {(x1, y1), (x0, y1)}, {(x0, y1), (x0, y0)}} 
def rectangle_to_sides(rectangle):
    A, B = rectangle
    x0, y0 = A
    x1, y1 = B
    a = sorted(((x0, y0), (x1, y0)))
    b = sorted(((x1, y0), (x1, y1)))
    c = sorted(((x1, y1), (x0, y1)))
    d = sorted(((x0, y1), (x0, y0)))
    return  sorted((a, b, c, d))


# --- Side rectangle Two coordinate rectangle to side rectangle ---
# x_min, y_min, x_max, y_max = min(x for x, _ in rect), min(y for _, y in rect), max(x for x, _ in rect), max(y for _, y in rect)
# ((x_min, y_min), (x_max, y_max))
def sides_to_rectangle(sides):
    all_x_in_sides = [x for side in sides for x, _ in side]
    all_y_in_sides = [y for side in sides for _, y in side]
    x_min, y_min = min(all_x_in_sides), min(all_y_in_sides)
    x_max, y_max = max(all_x_in_sides), max(all_y_in_sides)
    return [(x_min, y_min), (x_max, y_max)]


def is_rectangle_inside(rectangle):
    sub_rectangles = create_sub_rectangles(rectangle)
    return all(sub_rectangle in inside_rectangles for sub_rectangle in sub_rectangles)


def get_fence():
    return [sorted([a, b]) for a, b in zip(data[:-1], data[1:])] + [sorted([data[-1], data[0]])]


def part_2():
    outside_rectangles = set()
    searched_rectangles = set()

    fence_side_list = get_fence()
    total_rectangle = [(min(x_ticks), min(y_ticks)), (max(x_ticks), max(y_ticks))]

    total_rectangle_list = create_sub_rectangles(total_rectangle)
    rectangle_search_stack = [total_rectangle_list[0]]
    rectangle = rectangle_search_stack.pop(0)
    sides = rectangle_to_sides(rectangle)
    outside_rectangles.add(rectangle)
    if any(side in fence_side_list for in side for sides):
        



    print(total_rectangle_list[0])
    exit()


    print(fence)
    # main_set = create_sub_rectangles([(7,1), (11, 7)])
    # sub_set = create_sub_rectangles([(7,5), (9, 7)])
    sides = rectangle_to_sides([(7,5), (9, 7)])
    # rectangle = sides_to_rectangle(sides)
    sides.append( sorted( [(9, 5), (2, 5)] ) )
    # rectangle = sides_to_rectangle(sides)
    # sides = rectangle_to_sides([(7,5), (9, 7)])

    print(sides, sides[-1] in fence)
    

    exit()
    print(main_set)
    print(sub_set)
    print(sub_set[0] in main_set)
    print(rect)

    return None


# print('part 1:', part_1())
print('part 2:', part_2())


# --- Create list of inside rectangles and outsid rectangles ---
# Skapa en lista med alla sidor (mur)
# Skapa en lista (rect_list) med alla sidor i alla rektanglar (från x = 0 till x + 10, y = 0 och y + 10) [set och sorterad] (--> see "Rectangle to subrectanglses")
# Stacka up första rektangel (rect_stack) från vänstra hörnet.
# Popa första rektangeln från stacken och kolla om någon av sidorna matchar någon i muren
#   Om ej: Lägg till popade rektangeln i listan av outside_rectangle
#   Om   : Lägg till popade rektangeln i listan av inside_rectangle
# Om ej så leta up matchande rektangel sida bland rektangellistans (rect_list) sida och lägg denna till stacken (rect_stack).

# Get list of rectangles as from part-1
# Pop first rectangle and test
# Break down this rectangle into smaller rectangles (--> see "Rectangle to subrectanglses")
# Check if all thesse is are all inside rectangles (or none is on the outside rectangle list)

# --- Rectangle to subrectanglses ---
# Get all the x and y coordinates. x0, x1, x3...xn and y0, y1, y2, yn
# If big rect is (x0, y0), (xn, yn) 
#   --> (x0, y0), (x1, y1) * (x1, y0), (x2, y1) * (x2, y0), (x3, y1) ... (x[n-1], y0), (xn, y1)
#   --> (x0, y1), (x1, y2) * (x1, y1), (x2, y2) * (x2, y1), (x3, y2) ... (x[n-1], y1), (xn, y2)
#   --> (x0, y[n-1]), (x1, yn) * (x1, y[n-1]), (x2, yn) * (x2, y[n-1]), (x3, yn) ... (x[n-1], y[x-1]), (xn, yn)

# --- Two coordinate rectangle to side rectangle ---
# (x0, y0), (x1, y1) --> {{(x0, y0), (x1, y0)}, {(x1, y0), (x1, y1)}, {(x1, y1), (x0, y1)}, {(x0, y1), (x0, y0)}} 

# --- Side rectangle Two coordinate rectangle to side rectangle ---
# x_min, y_min, x_max, y_max = min(x for x, _ in rect), min(y for _, y in rect), max(x for x, _ in rect), max(y for _, y in rect)
# ((x_min, y_min), (x_max, y_max))







# Ta fram alla rektanglar från x = 0 till x + 10, y = 0 och y + 10
# Övre vänstra utanför
# Sätt denna i en lista med utanför
# Kolla vilka sidor av denna som matchar sidor i muren
# Om ej stacka up alla sidor som inte har sidor i muren 
# gå till sidan och sätt den nya till utanför