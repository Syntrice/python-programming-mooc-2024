# Write your solution here
 
def exercise_points(number_completed: int):
    return number_completed // 10
    
 
def grade(points: int):
    
    if points <= 14:
        return 0
    elif points <= 17:
        return 1
    elif points <= 20:
        return 2
    elif points <= 23:
        return 3
    elif points <= 27:
        return 4
    elif points <= 30:
        return 5
 
def mean(numbers: list):
    return sum(numbers) / len(numbers)
 
def pass_percentage(grades: list):
    return (len(grades) - grades.count(0)) / len(grades) * 100
 
def grade_distribution(grades: list):
    for grade in range(5, -1, -1):
        print(f"{grade}: {'*'*grades.count(grade)}")
 
def main():
    
    points = []
    grades = []
    
    while True:
        
        # Split string into exam points and exercises completed
        data = input("Exam points and exercises completed: ").split(" ")
        
        # Break if input empty
        if data[0] == "": break
        
        # Cast to int
        data = [int(numeric_string) for numeric_string in data]
        
        # Calculate total points
        total_points = (data[0] + exercise_points(data[1]))
        
        # Store points value
        points.append(total_points)
        
        # Cut off for low exam grades
        if data[0] < 10:
            grades.append(0)
            continue
        
        # Calculate grade and store
        grades.append(grade(total_points))
        
    print("Statistics:")
    print(f"Points average: {mean(points):.1f}")
    print(f"Pass percentage: {pass_percentage(grades):.1f}")    
    print("Grade distribution:")
    grade_distribution(grades)
        
        
        
            
    
    
    
main()