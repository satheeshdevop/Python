Number = [1, 4, 3, 8, 4, 9, 0, 2, 5, 7]
  
Even_number = [ num for num in Number if num % 2 == 0  ]
Even_number.sort()

print("Number = " ,Number)
print("Even number in the list = " ,Even_number)