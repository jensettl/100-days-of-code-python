# Topcis: Data Types, Numbers, Operations, Type Conversion, f-Strings

# [start:stop:stepover]
# print("Hello"[:-1:2])

# Mathematical Operations Order: PEMDAS

print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? €")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = int(input("How many people to split the bill? "))

# print(type(total_bill))
# print(type(percentage))

result = float(total_bill) * (1 + float(percentage) / 100) / int(people)

print(f"Each person should pay: €{round(result, 2)}")
