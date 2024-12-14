import util
grid = util.get_input().split("\n")

def valid(x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def ascending_neighbours(x, y):
    for dx, dy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if valid(dx, dy) and grid[dy][dx].isdigit() and int(grid[dy][dx]) == int(grid[y][x]) + 1:
            yield (dx, dy)

def find_nines(x, y):
    seen = set()
    nines = 0
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        seen.add((cx, cy))
        if grid[cy][cx] == "9":
            nines += 1
        for pos in ascending_neighbours(cx, cy):
            if pos not in seen:
                stack.append(pos)
    return nines

def find_paths(x, y):
    if grid[y][x] == "9":
        return 1
    return sum(find_paths(*pos) for pos in ascending_neighbours(x, y))

count = 0
rating = 0
for y, row in enumerate(grid):
    for x, val in enumerate(row):             
        if val == "0":
            count += find_nines(x, y)
            rating += find_paths(x, y)
print(count, rating)