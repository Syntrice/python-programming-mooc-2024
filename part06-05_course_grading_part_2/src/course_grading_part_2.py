# write your solution here

if True:
    # this is never executed
    student_info_path = input("Student information: ")
    exercise_data_path = input("Exercises completed: ")
    exam_data_path = input("Exam points: ")
else:
    # hard-coded input
    student_info_path = "students1.csv"
    exercise_data_path = "exercises1.csv"
    exam_data_path = "exam_points1.csv"

# read student info into dictionary
student_info = {}
with open(student_info_path) as file:
    for line in file:
        parts = line.split(";")
        
        if parts[0] == "id": continue
        
        student_info[parts[0]] = f"{parts[1].strip()} {parts[2].strip()}"
        
# read student exercise data into  dictionary
exercise_data = {}
with open(exercise_data_path) as file:
    for line in file:
        parts = line.split(";")
        
        if parts[0] == "id": continue
        
        exercise_data[parts[0]] = [int(part.strip()) for part in parts[1::]]
    

# read exam data into dictionay
exam_data = {}
with open(exam_data_path) as file:
    for line in file:
        parts = line.split(";")
        
        if parts[0] == "id": continue
        
        exam_data[parts[0]] = [int(part.strip()) for part in parts[1::]]
        
        
# calculate grades into dictionary
grades = {}
for pic in student_info.keys():
    total_points = sum(exercise_data[pic]) // 4 + sum(exam_data[pic])
    
    if (total_points <= 14): grade = 0
    elif (total_points <= 17): grade = 1
    elif (total_points <= 20): grade = 2
    elif (total_points <= 23): grade = 3
    elif (total_points <= 27): grade = 4
    elif (total_points >= 28): grade = 5
    
    grades[pic] = grade
    
# print student exercises completed
for pic, name in student_info.items():
    print(f"{name} {grades[pic]}")

