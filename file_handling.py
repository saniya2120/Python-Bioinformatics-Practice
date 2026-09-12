count = 0

with open("genes.txt" , "r") as file:
    for line in file:
        gene = line.strip()
        print(gene)
        count += 1

with open("genes_summary.txt" , "w") as file:
    file.write("Gene Analysis Summary\n")
    file.write("Total genes: " + str(count))

with open("expression.csv" , "r") as file:
    for row in file:
        print(row.strip())

with open("expression.csv", "r") as file:
    for row in file:
        parts = row.strip().split(",")
        print(parts)

with open("expression.csv", "r") as file:
    for row in file:
        parts = row.strip().split(",")
        print("Gene:", parts[0])
        print("Expression:", parts[1])

with open("expression.csv", "r") as file:
    next(file)

    for row in file:
        parts = row.strip().split(",")

        gene = parts[0]
        expression = float(parts[1])

        print("Gene:", gene)
        print("Expression:", expression)

with open("expression.csv", "r") as file:
    next(file)

    for row in file:
        parts = row.strip().split(",")

        gene = parts[0]
        expression = float(parts[1])

        if expression > 10:
            print("Gene:", gene)
            print("Expression:", expression)

expressions = []

with open("expression.csv", "r") as file:
    next(file)

    for row in file:
        parts = row.strip().split(",")
        gene = parts[0]
        expression = float(parts[1])
        expressions.append(expression)

print("Total genes:", len(expressions))
print("Highest expression:", max(expressions))
print("Lowest expression:", min(expressions))
print("Average expression:", sum(expressions) / len(expressions))

expressions = []
high_expression = []
low_expression = []

with open("expression.csv", "r") as file:
    next(file)

    for row in file:
        parts = row.strip().split(",")

        gene = parts[0]
        expression = float(parts[1])

        expressions.append(expression)

        if expression > 10:
            high_expression.append(gene)

        if expression < 10:
            low_expression.append(gene)

print("Total genes:", len(expressions))
print("Highest expression:", max(expressions))
print("Lowest expression:", min(expressions))
print("Average expression:", sum(expressions) / len(expressions))

print("Genes > 10:", high_expression)
print("Genes < 10:", low_expression)
