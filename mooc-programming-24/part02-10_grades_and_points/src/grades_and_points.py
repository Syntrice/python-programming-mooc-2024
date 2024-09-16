# Write your solution here
 
grade = int(input("How many points [0-100]:"))
 
if grade < 0 or grade > 100:
    grade = "impossible!"
elif grade < 50:
    grade = "fail"
elif grade < 60:
    grade = "1"
elif grade < 70:
    grade = "2"
elif grade < 80:
    grade = "3"
elif grade < 90:
    grade = "4"
elif grade <= 100:
    grade = "5"
    
print("Grade: " + grade)