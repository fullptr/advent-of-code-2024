with open("input.txt") as f:
    data = f.read().strip()
    
grid = data.split("\n")
width = len(grid[0])
height = len(grid)

directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

def find_xmas(x, y, dx, dy):
    if not ((0 <= x + 3 * dx < width) and (0 <= y + 3 * dy < height)):
        return False
    return "XMAS" == "".join(grid[y + i * dy][x + i * dx] for i in range(4))

def find_mas(x, y):
    if grid[y][x] != "A" or x in {0, width - 1} or y in {0, height - 1}:
        return False
    tl = grid[y - 1][x - 1]
    br = grid[y + 1][x + 1]
    tr = grid[y - 1][x + 1]
    bl = grid[y + 1][x - 1]
    return {tl, br} == {tr, bl} == {"M", "S"}
    
part1 = 0
part2 = 0
for y, row in enumerate(grid):
    for x, val in enumerate(row):
        for dx, dy in directions:
            if find_xmas(x, y, dx, dy):
                part1 += 1
        if find_mas(x, y):
            part2 += 1
print(part1, part2)