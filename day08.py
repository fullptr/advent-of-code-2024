from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
import util

data = util.get_input().split("\n")
width = len(data[0])
height = len(data)
    
def valid(vec: util.Vec2):
    return 0 <= vec.x < width and 0 <= vec.y < height
    
def get_antinodes_part1(v1: util.Vec2, v2: util.Vec2):
    x1 = (v1 * 2) - v2
    x2 = (v2 * 2) - v1
    return [x for x in [x1, x2] if valid(x)]

def get_antinodes_part2(v1: util.Vec2, v2: util.Vec2):
    diff = v2 - v1
    curr = v2
    while valid(curr):
        yield curr
        curr = curr + diff
        
    curr = v1
    while valid(curr):
        yield curr
        curr = curr - diff

antennas = defaultdict(list)
for y, row in enumerate(data):
    for x, val in enumerate(row):
        v = util.Vec2(x, y)
        if val != ".":
            antennas[val].append(v)
        
part1 = set()
part2 = set()
for a in antennas.values():
    for a1, a2 in combinations(a, 2):
        part1 |= set(get_antinodes_part1(a1, a2))
        part2 |= set(get_antinodes_part2(a1, a2))
        
print(len(part1))
print(len(part2))