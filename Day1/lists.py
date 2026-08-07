# Day 1 - Lists Practice

genes = ["TP53", "BRCA1", "EGFR", "MYC", "KRAS"]

print("Genes:", genes)

# Accessing elements
print("First gene:", genes[0])
print("Last gene:", genes[-1])

# Adding an element
genes.append("ALK")
print("After adding ALK:", genes)

# Removing an element
genes.remove("KRAS")
print("After removing KRAS:", genes)

# Number of genes
print("Number of genes:", len(genes))

# Checking if a gene exists
if "TP53" in genes:
    print("TP53 is present")

# Loop through the list
for gene in genes:
    print("Gene:", gene)

# Expression values
expression = [12.5, 8.1, 20.3, 15.6, 9.2]

print("Expression values:", expression)
print("Highest expression:", max(expression))
print("Lowest expression:", min(expression))
print("Average expression:", sum(expression) / len(expression))

# Expression values above 10
for value in expression:
    if value > 10:
        print("Above 10:", value)
