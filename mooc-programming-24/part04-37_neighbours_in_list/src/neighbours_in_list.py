# Write your solution here

def longest_series_of_neighbours(numbers):
    series_length = 1
    length_longest = 1
    
    for i in range(1,len(numbers)):
        if (abs(numbers[i-1] - numbers[i]) == 1):
            series_length += 1
        else:
            series_length = 1
            
        length_longest = max(length_longest, series_length)
            
    return length_longest
    
    
if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))
    