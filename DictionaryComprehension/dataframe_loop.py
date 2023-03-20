import pandas
student_dict = {
    "student":["Dev","James","Angela"],
    "score":[49,80,76]
}
data = pandas.DataFrame(student_dict)
print("Index      Name       Score")
for (index,row) in data.iterrows():
    print(f"{str(index)}         {str(row.student)}       {str(row.score)}")

