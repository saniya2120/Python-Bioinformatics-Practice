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