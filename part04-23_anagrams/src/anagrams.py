# Write your solution here

def anagrams(str1, str2):
    if (sorted(str1) == sorted(str2)):
        return True
    return False

if __name__ == "__main__":
    print(anagrams("house", "mouse"))