# Write your solution here
import string


def change_case(orig_string: str):

    new_string = ""

    for char in orig_string:
        if char.isupper():
            new_string += char.lower()
        elif char.islower():
            new_string += char.upper()
        else:
            new_string += char

    return new_string


def split_in_half(orig_string: str):
    return (orig_string[: len(orig_string) // 2], orig_string[len(orig_string) // 2 :])


def remove_special_characters(orig_string: str):
    new_string = ""
    allowed = string.ascii_letters + string.digits + " "

    for char in orig_string:
        if char not in allowed:
            continue

        new_string += char

    return new_string


if __name__ == "__main__":
    print(remove_special_characters("helo£$a"))
