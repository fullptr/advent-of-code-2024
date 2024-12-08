from dataclasses import dataclass

def get_input():
    with open("input.txt") as f:
        return f.read().strip()
    
@dataclass(frozen=True)
class Vec2:
    x: int
    y: int
    
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: int):
        return Vec2(self.x * scalar, self.y * scalar)