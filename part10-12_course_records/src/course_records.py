# tee ratkaisusi tänne


class Course:
    pass


class CourseList:
    def __init__(self) -> None:
        courses = []
        
    def add_course(self, course: Course):
        print("adding course...")
        
    def get_course(self, name: str):
        print("getting course...")


class CourseApplication:

    def __init__(self) -> None:
        course_list = CourseList()

    def add_course(self):
        print("adding course...")

    def print_course_data(self):
        print("printing course data...")

    def print_statistics(self):
        print("printing statistics...")

    def print_help(self) -> None:
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

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


application = CourseApplication()
application.execute()