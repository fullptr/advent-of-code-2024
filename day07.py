import operator
import itertools
with open("input.txt") as f:
    data = f.read().strip()
    
inputs = []
for line in data.split("\n"):
    target, vals = line.split(": ")
    inputs.append((int(target), [int(x) for x in vals.split()]))
    
def apply_ops_single(target, vals, op_list):
    x = vals[0]
    for op, val in zip(op_list, vals[1:]):
        x = op(x, val)
    return x
    
def apply_ops(target, vals, ops):
    for op_list in itertools.product(ops, repeat=len(vals) - 1):
        x = apply_ops_single(target, vals, op_list)
        if x == target:
            return True
    return False
        
def apply(ops):
    count = 0
    for target, vals in inputs:
        if apply_ops(target, vals, ops):
            count += target
    return count

print(apply([operator.add, operator.mul]))
print(apply([operator.add, operator.mul, lambda x, y: int(f"{x}{y}")]))