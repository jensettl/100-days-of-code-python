# Day 05 - PyPasswordGenerator
# Generate a random password with the length of the user's choice
# for loops, range()

import random

password = ""
password_length = int(input("How many characters would you like in your password?\n"))

for _ in range(1, password_length + 1):
    password += chr(random.randint(33, 126))

print(password)
