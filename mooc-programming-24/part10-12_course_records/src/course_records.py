# tee ratkaisusi tänne
from typing import Optional

class Course:
    def __init__(self, name: str, grade: int, credit: int) -> None:
        self.__name = name
        self.__grade = grade
        self.__credit = credit
        
    @property
    def name(self):
        return self.__name
    
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, new_grade: int):
        self.raise_grade(new_grade)
    
    @property
    def credit(self):
        return self.__credit
    
    @credit.setter
    def credit(self, new_credit: int):
        self.__credit = new_credit
    
    def raise_grade(self, new_grade: int):
        # grade can be raised but never lowered
        if self.__grade < new_grade:
            self.__grade = new_grade
            
    def __str__(self) -> str:
        return f"{self.name} ({self.credit} cr) grade {self.grade}"
    

class CourseList:
    def __init__(self) -> None:
        self.__courses: dict[str, Course] = {}
        
    def update_course(self, name: str, grade: int, credit: int) -> None:
        if name not in self.__courses: 
            self.__courses[name] = Course(name, grade, credit)
        else:
            self.__courses[name].credit = credit
            self.__courses[name].grade = grade
        
    def get_course(self, course_name: str) -> Optional[Course]:
        if course_name not in self.__courses:
            return None
        
        return self.__courses[course_name]
    
    def get_all_courses(self) -> Optional[Course]:
        if not bool(self.__courses):
            return None
            
        return self.__courses
    
    def get_statistics(self) -> Optional[dict[str]]:
        if not bool(self.__courses):
            return None
        
        statistics: dict = {}
        statistics["num_courses"] = len(self.__courses)
        statistics["total_credits"] = 0
        statistics["grade_distribution"] = {}
        
        grade_sum = 0
        for course in self.__courses.values():
            statistics["total_credits"] += course.credit
            grade_sum += course.grade
            if course.grade in statistics["grade_distribution"]:
                statistics["grade_distribution"][course.grade] += 1
            else:
                statistics["grade_distribution"][course.grade] = 1
                
        statistics["mean_grade"] = grade_sum / len(self.__courses)
        
        return statistics
            
class CourseApplication:

    def __init__(self) -> None:
        self.course_list = CourseList()

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credit = int(input("credits: "))
        self.course_list.update_course(name, grade, credit)

    def print_course_data(self):
        course = self.course_list.get_course(input("course: "))
        if course != None:
            print(course)
        else:
            print("no entry for this course")

    def print_statistics(self):
        statistics = self.course_list.get_statistics()
        print(f'{statistics["num_courses"]} completed courses, a total of {statistics["total_credits"]} credits')
        print(f'mean {statistics["mean_grade"]:.1f}')
        print("grade distribution")
        for i in range(5,0, -1):
            print(f"{i}: ",end="")
            if i in statistics["grade_distribution"]:
                print("x" * statistics["grade_distribution"][i], end="")
            print("")
        
        
    def print_help(self) -> None:
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
        print("")
        

    def execute(self):

        self.print_help()

        while True:
            command = input("command: ")
            match command:
                case "0":
                    break
                case "1":
                    self.add_course()
                case "2":
                    self.print_course_data()
                case "3":
                    self.print_statistics()
                case _:
                    self.print_help()
                    
            print("")


application = CourseApplication()
application.execute()

