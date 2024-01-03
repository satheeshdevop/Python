def compute_hcf (x, y):
    if x > y :
        print("y is smaller")
    else :
        print("x is smaller")    
        
    for i in range(x, y):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf 

num1 = int(input(' Enter the number : '))
num2 = int(input(' Enter the number : '))
print("The hcf of ", num1,"and" , num2 ,"is" , compute_hcf(num1, num2))