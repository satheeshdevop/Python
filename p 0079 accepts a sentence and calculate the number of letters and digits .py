satheesh = input("Enter the Letters and numbers :  ")

count_letters = 0
count_numbers = 0

for devops in satheesh:
    if devops.isalpha():
        count_letters += 1
    elif devops.isdigit():
        count_numbers += 1 
    
print(f" count_numbers : ", count_numbers)
print(f" count_letters : ",  count_letters)
print("Thank you :)  ")