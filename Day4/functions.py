def calculate_average(values):
    return sum(values) / len(values)

values = [12.5, 8.3, 20.1, 15.6, 7.8]

result = calculate_average(values)

print(result)

def find_maximum(values):
    return max(values)

values = [12.5, 8.3, 20.1, 15.6, 7.8]

result = find_maximum(values)

print(result)

def find_minimum(values): 
    return min(values) 

values = [12.5, 8.3, 20.1, 15.6, 7.8]

result = find_minimum(values) 

print(result)

def count_genes(genes):
    return len(genes)

genes = ["TP53", "BRCA1", "MYC"]

result = count_genes(genes)

print(result)

def count_above_threshold(values, threshold):
    count = 0

    for value in values:
        if value > threshold:
            count += 1

    return count


values = [12.5, 8.3, 20.1, 15.6, 7.8]
threshold = 10

result = count_above_threshold(values, threshold)

print(result)

def count_below_threshold(values, threshold):
    count = 0

    for value in values:
        if value < threshold:
            count += 1

    return count


values = [12.5, 8.3, 20.1, 15.6, 7.8]
threshold = 10

result = count_below_threshold(values, threshold)

print(result)

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32


temperature = 25

result = celsius_to_fahrenheit(temperature)

print(result)

def gene_present(genes, gene):
    return gene in genes


genes = ["TP53", "BRCA1", "EGFR"]

gene = "BRCA1"

result = gene_present(genes, gene)

print(result)