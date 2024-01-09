my_str = str(input("Enter the word: "))
words = [word.capitalize() for word in my_str.split()]

words.sort()

print("The sorted words are :")

for word in words :
    print(word)

