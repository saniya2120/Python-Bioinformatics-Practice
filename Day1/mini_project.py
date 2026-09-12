# Day 1 - Gene Expression Analyzer

expression = [12.5, 8.1, 20.3, 15.6, 9.2]

print(f"Highest Expression: {max(expression)}")
print(f"Lowest Expression: {min(expression)}")
print(f"Number of Genes: {len(expression)}")

total = sum(expression)
average = total / len(expression)

print(f"Average Expression: {average}")

high_count = 0

for value in expression:
    if value > 10:
        high_count += 1

print(f"Expression Above 10: {high_count}")

low_count = 0

for value in expression:
    if value < 10:
        low_count += 1

print(f"Expression Below 10: {low_count}")
