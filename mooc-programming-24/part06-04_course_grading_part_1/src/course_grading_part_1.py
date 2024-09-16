# write your solution here

if True:
    # this is never executed
    student_info_path = input("Student information: ")
    exercise_data_path = input("Exercises completed: ")
else:
    # hard-coded input
    student_info_path = "students1.csv"
    exercise_data_path = "exercises1.csv"

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
    
    
# print student exercises completed
for pic, name in student_info.items():
    print(f"{name} {sum(exercise_data[pic])}")
    

    