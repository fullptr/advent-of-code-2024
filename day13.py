import util, parse
def solve(a, b, c, d, e, f):
    det, x, y = a*d-c*b, d*e-c*f, a*f-b*e
    return 3 * x // det + y // det if x % det == 0 and y % det == 0 else 0

count1 = count2 = 0
pattern = "Button A: X+{:d}, Y+{:d}\nButton B: X+{:d}, Y+{:d}\nPrize: X={:d}, Y={:d}"
for machine in util.get_input().split("\n\n"):
    a, b, c, d, e, f = parse.parse(pattern, machine).fixed
    count1 += solve(a, b, c, d, e, f)
    count2 += solve(a, b, c, d, e + 10**13, f + 10**13)
print(count1, count2)