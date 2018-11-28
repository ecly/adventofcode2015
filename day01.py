with open("input", "r") as f:
    directions = f.read()
    print(directions.count("(") - directions.count(")"))

    pos = 0
    for idx, c in enumerate(directions):
        if c == "(":
            pos += 1
        if c == ")":
            pos -= 1
        if pos < 0:
            print(idx+1)
            break
