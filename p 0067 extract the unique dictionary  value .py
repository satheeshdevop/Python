dictionary =  {  's' : 10, 'a' : 20,  't' : 30, 'h' : 40 , 'i' : 50, 'h' : 70   }

satheesh = set()
for i in dictionary.values():
    satheesh.add(i)

unique_value = list(satheesh)

print(f" Unique value in the string  : {unique_value}")