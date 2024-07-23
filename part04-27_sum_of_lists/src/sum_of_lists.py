# Write your solution here

def list_sum(list1, list2):
    return [list1[i] + list2[i] for i in range(len(list1))]
    
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))