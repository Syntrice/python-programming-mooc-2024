# Write your solution here
 
letter1 = input("1st letter:")
letter2 = input("2nd letter:")
letter3 = input("3rd letter:")
 
if letter1 < letter2 < letter3:
    middle = letter2
if letter1 < letter3 < letter2:
    middle = letter3
if letter2 < letter1 < letter3:
    middle = letter1
if letter2 < letter3 < letter1:
    middle = letter3
if letter3 < letter1 < letter2:
    middle = letter1
if letter3 < letter2 < letter1:
    middle = letter2
    
print("The letter in the middle is " + middle)