import re              
def check_special_char(satheesh):
    special_character = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'
    if re.search (special_character, satheesh) :
        return True
    else :
        return False
    
input_string = str(input("Enter the string : "))

check_special_character = check_special_char(input_string)

if check_special_character :
    print(f"Entered string {input_string} is contained a special character")

else :
    print(f"Entered string {input_string} is not contains a  strings")


print("Thank you ")