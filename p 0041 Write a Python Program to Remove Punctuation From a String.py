punctuations = '''!@#$%^&*_-`~<>?",.'''

my_str = input("Enter the string : ")
no_punctuation =  ""
for char in my_str :
    if char not in punctuations :
        no_punctuation = no_punctuation + char
print(no_punctuation)


 