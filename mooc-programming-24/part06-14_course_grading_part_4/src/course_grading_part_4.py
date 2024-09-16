# tee ratkaisu tänne
# write your solution here

if True:
    # this is never executed
    student_info_path = input("Student information: ")
    exercise_data_path = input("Exercises completed: ")
    exam_data_path = input("Exam points: ")
    course_data_path = input("Course information: ")
else:
    # hard-coded input
    student_info_path = "students3.csv"
    exercise_data_path = "exercises3.csv"
    exam_data_path = "exam_points3.csv"
    course_data_path = "course3.txt"



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
        
# calculate grades and total points into dictionary
total_points = {}
grades = {}
for pic in student_info.keys():
    total = sum(exercise_data[pic]) // 4 + sum(exam_data[pic])
    
    if (total <= 14): grade = 0
    elif (total <= 17): grade = 1
    elif (total <= 20): grade = 2
    elif (total <= 23): grade = 3
    elif (total <= 27): grade = 4
    elif (total >= 28): grade = 5
    
    grades[pic] = grade
    total_points[pic] = total
    
# read course info

course_info = {}
with open(course_data_path) as file:
    for line in file:
        parts = line.split(":")
        course_info[parts[0].strip()] = parts[1].strip()

with open("results.txt", "w") as txt:
    with open("results.csv", "w") as csv:
        txt.write(f"{course_info['name']}, {course_info['study credits']} credits\n")
        txt.write("======================================\n")
        txt.write("{name:<30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade}\n"
        .format(name = "name", exec_nbr = "exec_nbr", exec_pts = "exec_pts.", exm_pts = "exm_pts.", tot_pts = "tot_pts.", grade = "grade"))
        for pic, name in student_info.items():
            txt.write(f"{name:<30}{sum(exercise_data[pic]):<10}{(sum(exercise_data[pic]) // 4):<10}{sum(exam_data[pic]):<10}{total_points[pic]:<10}{grades[pic]}\n")
            csv.write(f"{pic};{name};{grades[pic]}\n")

            
