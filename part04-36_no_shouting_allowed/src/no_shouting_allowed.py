# Write your solution here

def no_shouting(strings):
    result = []
    for string in strings:
        if string.isupper():
            continue
        result.append(string)
    return result
    
if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)