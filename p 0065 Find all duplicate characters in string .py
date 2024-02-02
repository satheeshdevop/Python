def find_duplicates(input_string):
    character_count = {}
    Duplicates = []
    for i in input_string :
        if i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1

    for i, count in character_count.items():
        if count > 1 :
            Duplicates.append(i)
    return Duplicates

input_string = str(input("Enter the string :"))

duplicate_characters = find_duplicates(input_string)

print(f"Duplicate characters : {duplicate_characters}")
print("Thank you :)")