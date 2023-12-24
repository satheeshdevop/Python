#Program 2
#Write a Python program to do arithmetical operations addition and division.


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


# Addition
sum_result = num1 + num2
print(f"         Addition of two number:                   {num1} + {num2} = {sum_result}")

#Subraction
sub_result = num1 - num2 
print(f"             Subraction of two number: {num1} - {num2} = {sub_result}")

#Multiplication
Mul_result = num1 * num2 
print(f"             Multiplication of two number : {num1} * {num2} = {Mul_result}")
# Division
num3 = float(input("Enter the dividend for division: "))
num4 = float(input("Enter the divisor for division: "))
if num4 == 0:
 print("Error: Division by zero is not allowed.")
else:
 div_result = num3 / num4 
 print(f"            Division: {num3} / {num4} = {div_result}")

 # modulation 
 Mod_result = num1 % num2 
 print(f"            Modulation of  two numbers : {num1} % {num2} = {Mod_result}")