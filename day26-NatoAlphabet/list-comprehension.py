# LIST Comprehension
# Python Sequence Types: List, Range, Tuple, String

list = [x * 2 for x in range(1, 5)]
print(list)

list_of_tuples = [(1, 2), (3, 1), (5, 4)]
new_list = [x + y for (x, y) in list_of_tuples]

print(new_list)


# DICTIONARY Comprehension

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
import random

student_grades = {
    student: random.choice(["A", "B", "C", "D", "E"]) for student in names
}

print([student for student in student_grades if student_grades[student] == "A"])

# iterate through PANDAS DataFrame
import pandas as pd

student_dict = {"student": ["Ale", "Beth", "Cece"], "score": [38, 72, 90]}

student_df = pd.DataFrame(student_dict)
print(student_df)

for index, row in student_df.iterrows():
    print(row.score)
