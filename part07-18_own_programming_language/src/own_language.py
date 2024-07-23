
def init_variables() -> dict:
    """Init all variables keyed A - Z in a dictionary with value of zero.

    Returns:
        dict: the resulting dictionary of variables
    """
    
    variables = {}
    
    for i in range(65, 91):
        variables[chr(i)] = 0
        
    return variables

def read_value(value: str, variables: dict) -> int:
    """ Read a value, which can either be a literal integer or a variable name from A to Z.

    Args:
        value (str): value to interpret
        variables (dict): the dictionary containing the variables to search

    Returns:
        int: the corresponding value, in integer format
    """
    if value.isnumeric():
        return int(value)
    else:
        return variables[value]

def read_locations(program: list) -> dict:
    """ Read the named locations in the code, and store them in a dictionary with the corresponding line number as values

    Args:
        program (list): the program to read

    Returns:
        dict: a dictionary mapping the names to their corresponding locations
    """
    locations = {}
    for i, line in enumerate(program):
        if ":" in line:
            locations[line[:len(line)-1]] = i
            
    return locations

def run(program: list):
    """
    
    Run a list of code lines, with the following commands to be interpreted:

    PRINT [value]: prints the value
    MOV [variable] [value]: assigns the value to the variable
    ADD [variable] [value]: adds the value to the variable
    SUB [variable] [value]: subtracts the value from the variable
    MUL [variable] [value]: multiplies the variable by the value
    [location]:: names a line of code, so it can be jumped to from elsewhere
    JUMP [location]: jumps to the location specified
    IF [condition] JUMP [location]: if the condition is true, jump to the location specified
    END: finish execution


    Args:
        program (list): a list containing the lines of the programs. Each line must correspond to one of the above instructions
    """
    
    variables = init_variables()
    locations = read_locations(program)
    output = []
    
    print(locations)
    
    current_line = 0
    while current_line < len(program):
        command = program[current_line].split(" ")
        
        print(f"{current_line}: {command}")
        
        match command[0]:
            case "PRINT":
                
                # prints the value to the output list
                output.append(read_value(command[1], variables))
                
            case "MOV":
                
                # assigns the value to the specified variable
                variables[command[1]] = read_value(command[2], variables)
                
            case "ADD":
                
                # adds the value to the specified variable
                variables[command[1]] += read_value(command[2], variables)
                
            case "SUB":
                
                # subtracts the value to the specified variable
                variables[command[1]] -= read_value(command[2], variables)
                
            case "MUL":
                
                # multiplies the value to the specified variable
                variables[command[1]] *= read_value(command[2], variables)
                
            case "JUMP":
                
                # jumps to the specified location
                current_line = locations[command[1]]
                continue
                
            case "IF":
                
                jump = False
                
                left = read_value(command[1], variables)
                right = read_value(command[3], variables)
                
                match command[2]:
                    case "==":
                        jump = left == right
                    case "!=":
                        jump = left != right
                    case "<":
                        jump = left < right
                    case "<=":
                        jump = left <= right
                    case ">":
                        jump = left > right
                    case ">=":
                        jump = left >= right
                
                if jump:
                    current_line = locations[command[5]]
                
            case "END":
                
                # goto end of execution, ending program
                
                current_line = len(program)
                continue
                
        current_line += 1
    
    return output
    
if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)

