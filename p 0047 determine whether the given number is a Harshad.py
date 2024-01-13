''' A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
In other words, a number is considered a Harshad number if it can be evenly divided by the
sum of its own digits.
For example:
18 is a Harshad number because , and 18 is divisible by 9
42 is not a Harshad number because , and 42 is not divisible by 6.
'''
def harshad_number(sum):    
    sum_of_digit = sum(int (i)  for i in str(num))
    return num % sum_of_digit  == 0

num = int(input("Enter the number : "))

if harshad_number(num):
    print(f"{num} is a Harshad number")
else:
    print(f"{num} is not Harshad number.")