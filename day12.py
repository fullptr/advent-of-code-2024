import util, collections, itertools
grid = util.get_input().split("\n")

def valid(x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def flood_fill(x, y):
    value = grid[y][x]
    garden = set()
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        garden.add((cx, cy))
        for dx, dy in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
            if valid(dx, dy) and (dx, dy) not in garden and grid[dy][dx] == value:
                stack.append((dx, dy))
    return garden

def get_gardens():
    remaining = {(x, y) for y, row in enumerate(grid) for x, _ in enumerate(row)}
    gardens = []
    while remaining:
        x, y = remaining.pop()
        garden = flood_fill(x, y)
        remaining -= garden
        gardens.append(garden)
    return gardens

def get_fences(area):
    c = collections.Counter()
    for (x, y) in area:
        c[x, y,   "H"] += 1
        c[x, y,   "V"] += 1
        c[x-1, y, "V"] += 1
        c[x, y-1, "H"] += 1
    return {key for key, value in c.items() if value == 1}

def calc_circumferance(area):
    return len(get_fences(area))

def calc_edges(area):
    fences = collections.defaultdict(list)
    
    # Collapse horizonally and vertically
    for x, y, d in get_fences(area):
        if d == "H":
            fences[y, d].append(x)
        else:
            fences[x, d].append(y)
            
    # There may be separate fences of each horizonal/vertical, so split them
    verticals = collections.defaultdict(list)
    horizontals = collections.defaultdict(list)
    fence_count = 0
    for (coord, direction), vals in fences.items():
        m = verticals if direction == "V" else horizontals
        lo = None
        hi = None
        for x in sorted(vals):
            if lo is None:
                lo = x
            if hi is not None and x - 1 != hi:
                m[coord].append((lo, hi))
                lo = x
            hi = x
        m[coord].append((lo, hi))
        fence_count += len(m[coord])
        
    # intersections add 2 to the count! >:( (because 2 overlapping fences is actually 4)
    h_lines = []
    for coord, fences in horizontals.items():
        for lo, hi in fences:
            h_lines.append((lo, hi + 1, coord + 1))
    v_lines = []
    for coord, fences in verticals.items():
        for lo, hi in fences:
            v_lines.append((lo, hi + 1, coord + 1))
    
    for h_line, v_line in itertools.product(h_lines, v_lines):
        h_y0, h_y1, h_x = h_line
        v_x0, v_x1, v_y = v_line
        if h_y0 < v_y < h_y1 and v_x0 < h_x < v_x1:
            fence_count += 2
    
    return fence_count

part1 = 0
part2 = 0
for garden in get_gardens():
    area = len(garden)
    circumferance = calc_circumferance(garden)
    edges = calc_edges(garden)
    part1 += area * circumferance
    part2 += area * edges
print(part1, part2)