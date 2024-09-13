# Write your solution here
import re

def is_dotw(my_string: str) -> bool:
    return bool(re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string))

def all_vowels(my_string: str) -> bool:
    return bool(re.search("^[aeiou]*$", my_string))

def time_of_day(my_string: str) -> bool:
    return bool(re.search("^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string))

if __name__ == "__main__":
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
    print(time_of_day("19:zz:04"))