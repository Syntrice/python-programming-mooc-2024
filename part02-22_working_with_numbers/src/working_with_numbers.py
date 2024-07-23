# Write your solution here
 
numbers = []
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number = int(input(""))
    if number == 0:
        break
    
    numbers.append(number)
 
print(f"Numbers typed in {len(numbers)}")
print(f"The sum of the numbers is {sum(numbers)}")
print(f"The mean of the numbers is {sum(numbers)/len(numbers)}")
 
negatives = 0
positives = 0
 
for number in numbers:
    if number < 0:
        negatives += 1
    else:
        positives += 1
        
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")