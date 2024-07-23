# Write your solution here
pin = 4321
attempts = 0
while True:
    attempts += 1
    if (int(input("PIN:")) == pin):
        if attempts == 1:
            print(f"Correct! It only took you one single attempt!")
            break
        else:
            print(f"Correct! It took you {attempts} attempts")
            break
    else:
        print("Wrong")
        continue