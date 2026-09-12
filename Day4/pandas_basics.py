import pandas as pd

data = {
    "Gene": ["TP53", "BRCA1", "MYC"],
    "Sample_1": [12.5, 8.3, 20.1],
    "Sample_2": [14.2, 9.1, 18.7],
    "Sample_3": [10.8, 7.5, 22.4]
}

df = pd.DataFrame(data)

print(df)
print("\nGenes:")
print(df["Gene"])

print("\nSample 1:")
print(df["Sample_1"])

print("\nAverage Sample 1 expression:")
print(df["Sample_1"].mean())

print("\nHighest Sample 1 expression:")
print(df["Sample_1"].max())

print("\nLowest Sample 1 expression:")
print(df["Sample_1"].min())

print("\nGenes with Sample 1 expression > 10:")
print(df[df["Sample_1"] > 10])