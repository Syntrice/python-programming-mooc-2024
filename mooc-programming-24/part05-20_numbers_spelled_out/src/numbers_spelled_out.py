# Write your solution here
 
def dict_of_numbers():
    numbers = {}
    
    # numbs 0 to 20
    nums_primary = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }
 
    nums_tens = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }
 
    for i in range(20):
        numbers[i] = nums_primary[i]
        
    for i in range(20,100):
        a, b = divmod(i, 10)
        
        if b != 0:
            numbers[i] = f"{nums_tens[a]}-{nums_primary[b]}"
        else:
            numbers[i] = nums_tens[a]
        
        
    return numbers
 
if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[90])
 
