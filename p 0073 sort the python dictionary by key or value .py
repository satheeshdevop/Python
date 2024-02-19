satheesh = {'m' : 1, 'l' : 2, 'o' : 5, 'p' : 6, 's' : 8}
sorted_satheesh = dict (sorted(satheesh.items()))

print("Sorted keys are :")

for keys, values in sorted_satheesh.items():
    print(f"{keys} : {values}")

print("Thank you :) ")

