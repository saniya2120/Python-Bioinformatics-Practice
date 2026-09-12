genes = ["TP53", "BRCA1", "MYC", "EGFR", "KRAS"]

expression = [12.5, 8.3, 20.1, 15.6, 7.8]
def count_genes(genes):
    return len(genes)


def calculate_average(values):
    return sum(values) / len(values)


def find_maximum(values):
    return max(values)


def find_minimum(values):
    return min(values)


def genes_above_threshold(genes, expression, threshold):
    result = []

    for i in range(len(genes)):
        if expression[i] > threshold:
            result.append(genes[i])

    return result


print("Number of genes:", count_genes(genes))
print("Average expression:", round(calculate_average(expression), 2))
print("Highest expression:", find_maximum(expression))
print("Lowest expression:", find_minimum(expression))
print("Genes above 10:", genes_above_threshold(genes, expression, 10))