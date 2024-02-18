from collections import OrderedDict

def check_order(string, reference):
    string = OrderedDict.fromkeys(string)
    reference = OrderedDict.fromkeys(reference)

    return string == reference 
    

input_string      =   "Satheesh_Devops"
reference_string  =   "satheesh_devops"

if check_order(input_string, reference_string):
    print("The order of characters in the input string matches the reference string .")
else:
    print("The order of characters in the input string not matches the reference ")


print("Thank you :)")