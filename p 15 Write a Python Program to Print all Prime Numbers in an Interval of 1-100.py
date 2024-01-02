lower_limit = 1 
higher_limit = 100
print(f"The prime number between", lower_limit ,"and", higher_limit ,"are  :"  )
for num in range (lower_limit, higher_limit + 1) :
    if num  > 1 :
       for  i in range(2, num):
         if ( num % i) == 0 :
          break
       else :
          print(num)
