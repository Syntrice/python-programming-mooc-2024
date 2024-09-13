class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"


def accepted(attempts: list[CourseAttempt]) -> list[CourseAttempt]:
    return list(filter(lambda x: x.grade >= 1, attempts))

def attempts_with_grade(attempts: list[CourseAttempt], grade: int) -> list[CourseAttempt]:
    return list(filter(lambda x: x.grade == grade, attempts))

def passed_students(attempts: list[CourseAttempt], course: str) -> list[str]:
    passed_course_attempts = filter(lambda x: x.course_name == course and x.grade > 0, attempts)
    passed_course_students = map(lambda x: x.student_name, passed_course_attempts)
    return sorted(passed_course_students)