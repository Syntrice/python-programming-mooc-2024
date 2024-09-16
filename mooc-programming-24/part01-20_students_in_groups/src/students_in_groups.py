# Write your solution here
 
students = int(input("How many students on the course? "))
desired_group_size = int(input("Desired group size? "))
 
print("Number of groups formed:", students // desired_group_size + (students % desired_group_size > 0))
