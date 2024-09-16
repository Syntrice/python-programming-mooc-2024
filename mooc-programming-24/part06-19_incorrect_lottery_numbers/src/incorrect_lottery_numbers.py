# Write your solution here



def filter_incorrect():
    with open("lottery_numbers.csv") as numbers, open("correct_numbers.csv", "w") as correct:
        for line in numbers:
            line = line.strip()
            parts = line.split(";")
            
            try:
                week = int(parts[0].split(" ")[1].strip())
                numbers = [int(x) for x in parts[1].split(",")]
                
                if len(numbers) < 7:
                    raise Exception
                
                for num in numbers:
                    if num < 1 or num > 39: raise Exception
                
                if not len(numbers) == len(set(numbers)):
                    raise Exception
            
            except:
                continue
            
            correct.write(line + "\n")
            
            
            
            
if __name__ == "__main__":
    filter_incorrect()