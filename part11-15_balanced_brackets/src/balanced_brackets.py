def balanced_brackets(my_string: str):
    
    # remove first character if it's not a bracket
    if not my_string[0] in "()[]":
        return balanced_brackets(my_string[1:])
    
    # remove last character if it's not a bracket
    if not my_string[-1] in "()[]":
        return balanced_brackets(my_string[:-1])
    
    # if the string is empty, we're done and it's verified balanced
    if len(my_string) == 0:
        return True
    
    # check if the first and last characters are matching round brackets, if so remove them and check the rest
    if my_string[0] == '(' and my_string[-1] == ')':
        # remove first and last character
        return balanced_brackets(my_string[1:-1])
    
    # check if the first and last characters are matching square brackets, if so remove them and check the rest
    if my_string[0] == '[' and my_string[-1] == ']':
        return balanced_brackets(my_string[1:-1])

    # this will be reached if the first and last characters are not matching brackets
    return False

if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)