from util import get_input, Vec2

def move_robot(grid, pos: Vec2, diff: Vec2):
    curr = Vec2(pos.x, pos.y)
    if grid[curr.y][curr.x] != "@":
        raise Exception("Tried to start at bad location")
    pushing = False
    while True:
        curr = curr + diff
        if grid[curr.y][curr.x] == "#":
            return pos # hit wall, nothing to do
        elif grid[curr.y][curr.x] == "O":
            pushing = True
            
        # found space
        elif pushing:
            grid[pos.y][pos.x] = "."
            grid[curr.y][curr.x] = "O"
            loc = pos + diff
            grid[loc.y][loc.x] = "@"
            return loc
        else:
            grid[pos.y][pos.x] = "."
            grid[curr.y][curr.x] = "@"
            return curr
        
def find_robot(grid):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == "@":
                return Vec2(x, y)
    raise Exception("Couldn't find robot")
        
def print_grid(grid):
    for row in grid:
        print("".join(row))
        
def calculate_gps(grid):
    count = 0
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val in {"O", "["}:
                count += 100 * y + x
    return count

def get_data():
    area, moves = get_input().split("\n\n")
    grid = []
    for row in area.split("\n"):
        grid.append([cell for cell in row])
    return grid, moves

def part1():
    grid, moves = get_data()        
    pos = find_robot(grid)
    for move in moves:
        if move == "^":
            pos = move_robot(grid, pos, Vec2(0, -1))
        elif move == ">":
            pos = move_robot(grid, pos, Vec2(1, 0))
        elif move == "<":
            pos = move_robot(grid, pos, Vec2(-1, 0))
        elif move == "v":
            pos = move_robot(grid, pos, Vec2(0, 1))
    print(calculate_gps(grid))
    
def expand_grid(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for val in row:
            if val == "#":
                new_row.extend(["#", "#"])
            if val == "O":
                new_row.extend(["[", "]"])
            if val == ".":
                new_row.extend([".", "."])
            if val == "@":
                new_row.extend(["@", "."])
        new_grid.append(new_row)
    return new_grid

def part2_can_move(grid, pos: Vec2, dp: Vec2):
    curr = Vec2(pos.x, pos.y)
    step = curr + dp
    
    if dp in {Vec2(1, 0), Vec2(-1, 0)}:
        if grid[step.y][step.x] == "#":
            return False
        elif grid[step.y][step.x] in {"[", "]"}:
            return part2_can_move(grid, step, dp)
        return True
    
    elif dp in {Vec2(0, 1), Vec2(0, -1)}:
        if grid[step.y][step.x] == "#":
            return False
        elif grid[step.y][step.x] == "[":
            diag = step + Vec2(1, 0)
            return part2_can_move(grid, step, dp) and part2_can_move(grid, diag, dp)
        elif grid[step.y][step.x] == "]":
            diag = step + Vec2(-1, 0)
            return part2_can_move(grid, step, dp) and part2_can_move(grid, diag, dp)
        return True
    
    else:
        raise Exception("Invalid direction")
    
def part2_do_move(grid, pos: Vec2, dp: Vec2, moved: set[Vec2]):
    if pos in moved:
        return pos
    
    if grid[pos.y][pos.x] == "#":
        raise Exception("Tried to move a #")
    
    curr = Vec2(pos.x, pos.y)
    step = curr + dp
    
    if grid[step.y][step.x] in {"[", "]"}:
        part2_do_move(grid, step, dp, moved)
        
    grid[step.y][step.x] = grid[curr.y][curr.x]
    moved.add(curr)
    
    if dp in {Vec2(0, 1), Vec2(0, -1)}: 
        if grid[curr.y][curr.x] == "[":
            side = curr + Vec2(1, 0)
            part2_do_move(grid, side, dp, moved)
            
        if grid[curr.y][curr.x] == "]":
            side = curr + Vec2(-1, 0)
            part2_do_move(grid, side, dp, moved)
       
    grid[curr.y][curr.x] = "."
    return step
       
def part2():
    grid, moves = get_data()
    grid = expand_grid(grid)    
    pos = find_robot(grid)
    for move in moves:
        moved = set()
        if move == "^" and part2_can_move(grid, pos, Vec2(0, -1)):
            pos = part2_do_move(grid, pos, Vec2(0, -1), moved)
        elif move == ">" and part2_can_move(grid, pos, Vec2(1, 0)):
            pos = part2_do_move(grid, pos, Vec2(1, 0), moved)
        elif move == "<" and part2_can_move(grid, pos, Vec2(-1, 0)):
            pos = part2_do_move(grid, pos, Vec2(-1, 0), moved)
        elif move == "v" and part2_can_move(grid, pos, Vec2(0, 1)):
            pos = part2_do_move(grid, pos, Vec2(0, 1), moved)
    print(calculate_gps(grid))

def main():    
    part1()
    part2()
 
main()