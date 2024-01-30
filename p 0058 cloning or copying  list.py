l = [1, 5, 3, 6, 2]

cloned_list_using_slice_operator = l[:]

cloned_list_using_list_operator = list(l)

cloned_list_using_list_comprehension = [i for i in l]



print("cloned_list_using_list_operator) : ",cloned_list_using_list_operator)
print("cloned_list_using_slice_operator : ",cloned_list_using_slice_operator)
print("cloned_list_using_list_comprehension : ",cloned_list_using_list_comprehension)