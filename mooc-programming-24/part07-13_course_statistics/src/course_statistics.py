# Write your solution here

import urllib.request as ureq
import json

# data is in format [{course},{course},{course}]


def retrieve_all():

    # open the url, returning a response object
    request = ureq.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")

    # prase the url response data into json intepreter
    course_data = json.loads(request.read())

    # append the active courses to a list of tuples with corresponding data
    active_courses = []
    for course in course_data:

        # continue if course is disabled
        if course["enabled"] == False:
            continue

        active_courses.append(
            (
                course["fullName"],
                course["name"],
                course["year"],
                sum(course["exercises"]),
            )
        )

    return active_courses


def retrieve_course(course_name: str):

    request = ureq.urlopen(
        f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    )
    course_data = json.loads(request.read())

    students = 0
    hours = 0
    exercises = 0

    for week in course_data.values():
        if week["students"] > students:
            students = week["students"]

        hours += week["hour_total"]
        exercises += week["exercise_total"]

    return {
        "weeks": len(course_data),
        "students": students,
        "hours": hours,
        "hours_average": hours // students,
        "exercises": exercises,
        "exercises_average": exercises // students,
    }


if __name__ == "__main__":
    print(retrieve_course("docker2019"))
