with open("input", "r") as f:
    directions = f.read()
    print(directions.count("(") - directions.count(")"))
