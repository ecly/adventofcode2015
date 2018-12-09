import sys

total_paper = 0
dims = list(map(lambda l: list(map(int, l.split("x"))), sys.stdin.readlines()))
for l, w, h in dims:
    s1 = l * w
    s2 = w * h
    s3 = h * l
    total_paper += 2 * (s1 + s2 + s3) + min(s1, s2, s3)

print(total_paper)

total_ribbon = 0
for l, w, h in dims:
    min1, min2, _ = sorted([l, w, h])
    bow = l * w * h
    total_ribbon += 2 * (min1 + min2) + bow

print(total_ribbon)
