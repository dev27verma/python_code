def average_height(student_heights):
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])
    return student_heights


student_heights = input("Input a list of student heights in cm ").split(',')
print(f"Student Height In List: {average_height(student_heights)}")
print(f"Average Height of the students: {round(sum(average_height(student_heights)) / len(average_height(student_heights)))}")
