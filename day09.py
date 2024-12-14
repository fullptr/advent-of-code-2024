import util, itertools
from dataclasses import dataclass
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

@dataclass
class File:
    loc: int
    file_id: int
    size: int

def expand2(string):
    files = []
    loc = 0
    file_id = 0
    for idx, x in enumerate(string):
        if idx % 2 == 0:
            files.append(File(loc=loc, file_id=file_id, size=int(x)))
            file_id += 1
        else:
            pass
        loc += int(x)
    return files

def compress2(files):
    copy = [f for f in files]
    for file in reversed(files):
        # Attempt to find space inbetween two files
        for idx, (f1, f2) in enumerate(itertools.pairwise(copy)):
            if f1 == file: break
            space = f2.loc - f1.loc - f1.size
            if file.size <= space:
                file.loc = f1.loc + f1.size
                copy.remove(file)
                copy.insert(idx+1, file)
                break
    return copy

def checksum2(files):
    checksum = 0
    for file in files:
        for idx in range(file.loc, file.loc + file.size):
            checksum += idx * file.file_id
    return checksum
        
l = expand(data)
l = compress(l)
print(sum(i * x for i, x in enumerate(l)))

files = expand2(data)
files = compress2(files)
print(checksum2(files))