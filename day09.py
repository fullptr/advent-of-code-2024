import util
from queue import SimpleQueue
data = util.get_input()

def expand(string):
    disk = []
    digit = 0
    for idx, char in enumerate(string.strip()):
        if idx % 2 == 0:
            disk.extend([digit for _ in range(int(char))])
            digit += 1
        else:
            disk.extend(["." for _ in range(int(char))])
    return disk
        

def compress(disk):
    def get_free_spaces():
        for idx, elem in enumerate(disk):
            if elem == ".":
                yield idx
        
    free_list = get_free_spaces()        
    for idx in range(len(disk) - 1, -1, -1):
        if disk[idx] == ".":
            continue
        slot = next(free_list)
        if slot > idx:
            break
        disk[slot], disk[idx] = disk[idx], disk[slot]
    return disk[:slot]
        
l = expand(data)
l = compress(l)
print(sum(i * x for i, x in enumerate(l)))