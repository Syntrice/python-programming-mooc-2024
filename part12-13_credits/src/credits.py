from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(attempts: list[CourseAttempt]) -> int:
    credit_sum = reduce(lambda reduced_sum, item: reduced_sum + item.credits, attempts, 0)
    return credit_sum

def sum_of_passed_credits(attempts: list[CourseAttempt]) -> int:
    passed_courses = filter(lambda x: x.grade >= 1, attempts)
    credit_sum = reduce(lambda reduced_sum, item: reduced_sum + item.credits, passed_courses, 0)
    return credit_sum

def average(attempts: list[CourseAttempt]) -> float:
    passed_courses = list(filter(lambda x: x.grade >= 1, attempts))
    grade_sum = reduce(lambda reduced_sum, item: reduced_sum + item.grade, passed_courses, 0)
    average_grade = grade_sum / len(passed_courses)
    return average_grade

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)