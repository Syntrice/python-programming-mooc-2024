# Write your solution here
password = input("Password:")
while True:
    repeat_password = input("Repeat password:")
    
    if password == repeat_password:
        print("User account created!")
        break
    else:
        print("They do not match!")
        continue