def check_binary_string(Dev):
    for i in Dev :
        if i not in '01' :
            return False
    return True

Dev = str(input("Enter the string :"))

if check_binary_string(Dev):
    print(f" {Dev} is Binary string ")
else :
    print(f" {Dev} is not a Binary string ")

print("Thank you :)")