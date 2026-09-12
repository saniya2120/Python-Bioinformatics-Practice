# Day 1 - Dictionary Practice

gene_expression = {
    "TP53": 12.4,
    "BRCA1": 8.6,
    "EGFR": 15.2,
    "MYC": 18.1,
    "KRAS": 6.9
}

# Accessing a value
print("TP53 expression:", gene_expression["TP53"])

# Number of genes
print("Number of genes:", len(gene_expression))

# Add a gene
gene_expression["ALK"] = 11.5
print("After adding ALK:", gene_expression)

# Loop through dictionary
for gene, expression in gene_expression.items():
    print(gene, ":", expression)

# Highly expressed genes
for gene, expression in gene_expression.items():
    if expression > 10:
        print("Highly expressed:", gene, expression)

# Total and average expression
total = sum(gene_expression.values())
average = total / len(gene_expression)

print("Total expression:", total)
print("Average expression:", average)

# Highest and lowest expressed genes
highest_gene = max(gene_expression, key=gene_expression.get)
lowest_gene = min(gene_expression, key=gene_expression.get)

print("Highest gene:", highest_gene)
print("Lowest gene:", lowest_gene)
