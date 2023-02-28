import pandas
student_dict = {
    "student":["Dev","James","Angela"],
    "score":[49,80,76]
}
data = pandas.DataFrame(student_dict)

for (index,row) in data.iterrows():
    print(row)
    print(index)
    print(row.student)
    print(row.score)

