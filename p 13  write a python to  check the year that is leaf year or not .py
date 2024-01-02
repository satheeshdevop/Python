leaf_year = int(input("Enter the number of year :  "))
print("Processing...")
if (leaf_year % 4 == 0) :
    print(f"Entered year : {leaf_year}  is leaf year")
else :
    print(f"Entered year : {leaf_year} is not a leaf year")