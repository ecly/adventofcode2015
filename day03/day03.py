from collections import defaultdict

def step(c, x, y):
    if c == ">":
        x += 1
    elif c == "<":
        x -= 1
    elif c == "v":
        y += 1
    elif c == "^":
        y -= 1

    return x, y


def part1(puzzle):
    houses = defaultdict(int)
    x, y = 0, 0
    houses[x, y] += 1
    for c in puzzle:
        x, y = step(c, x, y)
        houses[x, y] += 1

    return len(houses)


def part2(puzzle):
    houses = defaultdict(int)
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    houses[x1, y1] += 1

    is_santa = True
    for c in puzzle:
        if is_santa:
            x1, y1 = step(c, x1, y1)
            houses[x1, y1] += 1
            is_santa = False
        else:
            x2, y2 = step(c, x2, y2)
            houses[x2, y2] += 1
            is_santa = True

    return len(houses)


puzzle = input().strip()
print(part1(puzzle))
print(part2(puzzle))
