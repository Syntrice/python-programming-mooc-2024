# Write your solution here

def filter_solutions():
    correct = []
    incorrect = []
    
    with open("solutions.csv") as file:
        for line in file:
            line = line.strip()
            parts = line.split(";")
            
            if "+" in parts[1]:
                problem = parts[1].split("+")
                result = int(problem[0]) + int(problem[1])
            if "-" in parts[1]:
                problem = parts[1].split("-")
                result = int(problem[0]) - int(problem[1])
            
            if result == int(parts[2]):
                correct.append(line)
            else:
                incorrect.append(line)
                
    with open("correct.csv", "w") as file:
        for item in correct:
            file.write(item + "\n")
            
    with open("incorrect.csv", "w") as file:
        for item in incorrect:
            file.write(item + "\n")
            
# might be better to open them in parallel