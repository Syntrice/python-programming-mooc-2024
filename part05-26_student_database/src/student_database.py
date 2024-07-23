# Write your solution here

def add_student(db: dict, name: str):
    """ add a student to the database
    """
    db[name] = []

def print_student(db: dict, name: str):
    """ prints out information of a single student
    """
    
    # check if student exists in database
    if name not in db:
        print(name + ": no such person in the database")
        return
        
    print(name + ":")
    
    # check if student has completed any courses
    if len(db[name]) == 0:
        print(" no completed courses")
        return
    
    # list completed courses 
    print(f" {len(db[name])} completed courses:")
    
    grade_sum = 0
    for course in db[name]:
        print(f"  {course[0]} {course[1]}")
        grade_sum += course[1]
        
    # print average grade
    print(f" average grade {grade_sum / len(db[name])}")
        
        
def add_course(db: dict, name: str, course: tuple):
    """ adds course information to a single student
    """
    
    # check if student exists in database
    if name not in db:
        print(name + ": no such person in the database")
        return
    
    # ignore if grade is equal to 0
    if course[1] == 0:
        return
    
    # check if course already in database. If so, update grade if higher
    for i in range(len(db[name])):
        if db[name][i][0] == course[0]:
            if (course[1] > db[name][i][1]):
                db[name][i] = course
            return
    
    db[name].append(course)
    
def summary(db: dict):
    
    most_completed = (0, None)
    best_average = (0, None)
    
    for student, courses in db.items():
        if len(courses) > most_completed[0]:
            most_completed = (len(courses), student)
        
        grade_sum = 0;
        for course in courses:
            grade_sum += course[1]
            
        average = grade_sum / len(courses)
        
        if average > best_average[0]:
            best_average = (average, student)
    
    
    print(f"students {len(db)}")
    print(f"most courses completed {most_completed[0]} {most_completed[1]}")
    print(f"best average grade {best_average[0]} {best_average[1]}")
    
    


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)