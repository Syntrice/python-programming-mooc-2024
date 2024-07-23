# Write your solution here
 
def same_chars(string, i1, i2):
    if i1 >= len(string) or i2 >= len(string): return False
    return string[i1] == string[i2] 
 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))