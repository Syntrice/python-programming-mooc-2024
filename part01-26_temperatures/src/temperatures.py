# Write your solution here
fahrenheit = int(input("Please type in a temperature (F):"))
celsius = 5 / 9 * (fahrenheit - 32)
print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
    print("Brr! It's cold in here!")