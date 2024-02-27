satheesh = input("Enter the Comma separated sequence : ")

kumar = satheesh.split(',')

sorted_kumar = sorted(kumar)

sorted_sequence = ','.join(sorted_kumar)

print( f"sorted_sequence :  {sorted_sequence} "  )

print("Thank you :)  ")