nterm = int(input("How many term ? "))
n1, n2 = 0,1 
count = 0 
if nterm  <= 0 :
    print("Please enter a positive number")
elif nterm == 1 :
    print("Finonacci series upto",nterm,":")
    print(n1)
else :
    print("Fibonacci sequence :")
    while count < nterm :
        print(n1)
        nth =  n1 + n2 
        n1 = n2 
        n2 = nth
        count += 1