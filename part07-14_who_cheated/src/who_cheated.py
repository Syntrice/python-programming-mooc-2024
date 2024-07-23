# Write your solution here

import csv
from datetime import datetime, timedelta


def load_student_data() -> dict:

    students_data = {}
    with open("start_times.csv") as f_start_times:
        for student in csv.reader(f_start_times, delimiter=";"):
            students_data[student[0]] = {}
            students_data[student[0]]["start_time"] = datetime.strptime(
                student[1], "%H:%M"
            )

    with open("submissions.csv") as f_submissions:
        for submission in csv.reader(f_submissions, delimiter=";"):

            if "submissions" not in students_data[submission[0]]:
                students_data[submission[0]]["submissions"] = []

            data = {
                "task": submission[1],
                "points": submission[2],
                "time": datetime.strptime(submission[3], "%H:%M"),
            }

            students_data[submission[0]]["submissions"].append(data)

    return students_data


def cheaters() -> list[str]:
    """ Returns a list of students who have cheated. 
    That is, taken longer than 3 hours to submit their assignment

    Returns:
        list[str]: a list of the names of students who have cheated.
    """
    cheating_students = []

    students_data = load_student_data()

    for name, data in students_data.items():

        for exercise in data["submissions"]:

            if exercise["time"] - data["start_time"] > timedelta(hours=3):
                cheating_students.append(name)
                break

    return cheating_students

if __name__ == "__main__":
    print(cheaters())
    print(load_student_data())
