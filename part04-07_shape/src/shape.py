# Copy here code of line function from previous exercise and use it in your solution
 
def shape(tri_size, tri_char, rect_height, rect_char):
    for i in range(1, tri_size + 1):
        line(i,tri_char)
    for i in range(rect_height):
        line(tri_size,rect_char)
 
 
def line(length, character):
    if character == "":
        character = "*"
    print(character[0] * length)
 
 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")