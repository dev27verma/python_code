student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

print(student_scores)

student_grade = {}


for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grade[student] = "Outstanding"
    elif score > 80 and score < 91:
        student_grade[student] = "Exceeds Expectation"
    elif score > 71 and score < 81:
        student_grade[student] =  "Acceptable"
    else:
        student_grade[student] = "fail"

print(student_grade)