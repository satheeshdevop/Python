def find_words(words, k):
    result = []
    for i in words :
        if len(i) > k:
            result.append(i)
    return result
word_list = ["banana", "apple", "cherry", "date", "drager"]
k = 5
long_words = find_words(word_list, k)
print(f"words are longer than {k} characters : {long_words}")
