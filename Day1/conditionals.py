# Day 1 - Conditional Statements and Logical Operators

# Pass / Fail
marks = 82

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# Grade
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")


# Gene expression level
gene_expression = 17

if gene_expression >= 15:
    print("High")
elif gene_expression >= 10:
    print("Medium")
else:
    print("Low")


# Temperature checker
temperature = 38

if temperature >= 39:
    print("High Fever")
elif temperature >= 37:
    print("Mild Fever")
else:
    print("Normal")


# Even or Odd
number = 17

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Positive, Negative or Zero
number = -8

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Logical operators
age = 21
is_student = True

if age >= 18 and is_student:
    print("Adult Student")
else:
    print("Not an Adult Student")


# DNA base
base = "A"

if base == "A" or base == "G":
    print("Purine")
elif base == "C" or base == "T":
    print("Pyrimidine")
else:
    print("Invalid DNA Base")


# Login
username = "Saniya"
password = "Python123"

if username == "Saniya" and password == "Python123":
    print("Login Successful")
else:
    print("Invalid Username or Password")


# Not operator
logged_in = False

if not logged_in:
    print("Please Login")
else:
    print("Welcome")
