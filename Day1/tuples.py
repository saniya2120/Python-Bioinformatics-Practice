# Day 1 - Tuples Practice

genes = ("TP53", "BRCA1", "EGFR", "MYC", "KRAS")

print("Genes:", genes)

# Accessing elements
print("First gene:", genes[0])
print("Last gene:", genes[-1])

# Number of genes
print("Number of genes:", len(genes))

# Checking if a gene exists
if "TP53" in genes:
    print("TP53 is present")

# Loop through the tuple
for gene in genes:
    print("Gene:", gene)

# Expression data
expression = (12.5, 8.1, 20.3, 15.6, 9.2)

print("Highest expression:", max(expression))
print("Lowest expression:", min(expression))
print("Average expression:", sum(expression) / len(expression))
