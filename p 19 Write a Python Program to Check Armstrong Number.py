num = int(input("Enter a number : "))
num_string = str(num)
num_digits = len(num_string)

sum_of_powers = 0 
temp_num = num 

while temp_num > 0:
    digits =  temp_num % 10 
    sum_of_powers += digits ** num_digits
    temp_num //= 10

if sum_of_powers == num :
    print("f{num} is Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
