from collections import Counter
from bisect import insort
with open("day01_input.txt") as f:
    data = f.read().strip()
    
l = []
r = []
for line in data.split("\n"):
    a, b = line.split()
    insort(l, int(a))
    insort(r, int(b))
    
counts = Counter(r)
print(sum(abs(b - a) for a, b in zip(l, r)))
print(sum(a * counts[a] for a in l))