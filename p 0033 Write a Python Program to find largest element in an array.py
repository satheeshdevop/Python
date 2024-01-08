def find_largest_element(arr):
    if not arr : 
        return "Array is empty "
    largest_element = arr[0]
    for element in arr :
        if element in arr :
            if element > largest_element:
             largest_element = element 
    return largest_element
my_array = [2334, 233, 2334, 3432, 3243, 2343]
result = find_largest_element(my_array)
print(f"The largest number in the array is : {result}")