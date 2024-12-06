from functools import cmp_to_key
with open("input.txt") as f:
    data = f.read().strip()
    
def lines():
    for line in data.split("\n"):
        yield line
l = lines()
    
rules = []
for line in l:
    if line == "":
        break
    rules.append([int(x) for x in line.split("|")])
    
updates = []
for line in l:
    updates.append([int(x) for x in line.split(",")])
    
def is_sorted(update):
    scores = {value: idx for idx, value in enumerate(update)}
    for lhs, rhs in rules:
        if lhs in scores and rhs in scores and scores[rhs] < scores[lhs]:
            return False
    return True

def comparator(lhs, rhs):
    if [lhs, rhs] in rules:
        return -1
    if [rhs, lhs] in rules:
        return 1
    return 0

part1_count = 0
part2_count = 0
for update in updates:
    if is_sorted(update):
        part1_count += update[len(update) // 2]
    else:
        update = sorted(update, key=cmp_to_key(comparator))
        part2_count += update[len(update) // 2]
print(part1_count, part2_count)