import sys
from collections import Counter, defaultdict
vowels = "aeiou"
bad_subs = ["ab", "cd", "pq", "xy"]
def is_nice1(chars):
    if len([c for c in chars if c in vowels]) < 3:
        return False
    if all(x != y for x, y in zip(chars, chars[1:])):
        return False
    if any(bad in chars for bad in bad_subs):
        return False

    return True

def is_nice2(chars):
    if all(x != y for x, y in zip(chars, chars[2:])):
        return False

    pairs = defaultdict(list)
    for idx, (x, y) in enumerate(zip(chars, chars[1:])):
        if (x, y) not in pairs:
            pairs[x, y].append(idx)
        else:
            seen = pairs[x, y]
            if any(idx - seen_idx > 1 for seen_idx in seen):
                return True

    return False


lines = sys.stdin.readlines()
print(len(list(filter(is_nice1, lines))))
print(len(list(filter(is_nice2, lines))))
