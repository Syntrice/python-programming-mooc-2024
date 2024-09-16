# Write your solution here

# Write your solution here

import csv
from datetime import datetime, timedelta

def load_student_data() -> dict:
    """Loads student data into a dictionary structure

    Returns:
        dict: the dictionary containing student data for start times and submissions
    """

    students_data = {}
    with open("start_times.csv") as f_start_times:
        for student in csv.reader(f_start_times, delimiter=";"):
            
            # decode
            name = student[0]
            start_time = student[1]
            
            students_data[name] = {}
            students_data[name]["start_time"] = datetime.strptime(
                start_time, "%H:%M"
            )

    with open("submissions.csv") as f_submissions:
        for submission in csv.reader(f_submissions, delimiter=";"):
            
            # decode
            name = submission[0]
            task = submission[1]
            points = int(submission[2])
            time = submission[3]

            # append new dictionary if no submissions already recorded
            if "submissions" not in students_data[name]:
                students_data[name]["submissions"] = {}
            
            # ignore submission if made over 3 hours since the start time
            time = datetime.strptime(time, "%H:%M") 
            if time - students_data[name]["start_time"] > timedelta(hours=3):
                continue
            
            # if the submission task already exists, only add if the points are higher than current submission
            if task in students_data[name]["submissions"]:
                if students_data[name]["submissions"][task]["points"] > points:
                    continue
        
            data = {
                "points": points,
                "time": time,
            }

            students_data[name]["submissions"][task] = data

    return students_data

def final_points() -> dict:
    """ Returns a dictionary containing the final points for all students who did not cheat

    Returns:
        dict: a dictionary containing the final points for each legitimate student
    """
    
    final_points = {}
    
    students_data = load_student_data()
    
    for name, data in students_data.items():
        points = 0
        for exercise in data["submissions"].values():
            points += exercise["points"]
        
        final_points[name] = points
    
    return final_points
        
    

if __name__ == "__main__":
    print(final_points())