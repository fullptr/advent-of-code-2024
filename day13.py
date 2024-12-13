import util, parse

def solve(a, b, c, d, e, f):
    det = a*d-c*b
    x = d*e-c*f
    y = a*f-b*e
    if x % det == 0 and y % det == 0:
        return 3 * x // det + y // det

count1 = count2 = 0
pattern = "Button A: X+{:d}, Y+{:d}\nButton B: X+{:d}, Y+{:d}\nPrize: X={:d}, Y={:d}"
for machine in util.get_input().split("\n\n"):
    a, b, c, d, e, f = parse.parse(pattern, machine).fixed
    if ans := solve(a, b, c, d, e, f):
        count1 += ans
    if ans := solve(a, b, c, d, e + 10000000000000, f + 10000000000000):
        count2 += ans
print(count1, count2)