from itertools import pairwise
with open("input.txt") as f:
    data = f.read().strip()
    
def part1(values):
    diffs = [b - a for a, b in pairwise(values)]
    same_sign = all(x > 0 for x in diffs) or all(x < 0 for x in diffs)
    small_values = all(1 <= abs(x) <= 3 for x in diffs)
    return same_sign and small_values
    
def part2(v):
    return any(part1(v[:i] + v[i+1:]) for i in range(len(v)))
    
p1 = p2 = 0
for line in data.split("\n"):
    values = [int(x) for x in line.split()]
    full_line = part1(values)
    p1 += 1 if full_line else 0
    p2 += 1 if full_line or part2(values) else 0
print(p1, p2)