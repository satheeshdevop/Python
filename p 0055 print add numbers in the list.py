Number = [1, 4, 3, 8, 4, 9, 0, 2, 5, 7]
Add_number  = [ num for num in Number if num % 2 != 0 ]
Even_number = [ num for num in Number if num % 2 == 0  ]
print("Number = " ,Number)
print("Add number in the list = " ,Add_number)
print("Even number in the list = " ,Even_number)