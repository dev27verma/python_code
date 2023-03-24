student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
print(student_scores)
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if 100 >= student_scores[student] >= 91:
        student_grades[student] = "Outstanding"
    elif 90 >= student_scores[student] >= 81:
        student_grades[student] = "Exceeds Expectation"
    elif 80 >= student_scores[student] >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
