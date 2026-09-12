with open("expression.csv", "r") as file:
    next(file)

    for row in file:
        parts = row.strip().split(",")

        gene = parts[0]
        expression = float(parts[1])

        print("Gene:", gene)
        print("Expression:", expression)

        if expression > 10:
            print("High expression")