def uncommon_words(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())
    uncommon_words_set = words1.symmetric_difference(words2)

    uncommon_word_list = list(uncommon_words_set)
    return uncommon_word_list 
string1 = "Hello I am satheesh devops"
string2 = "Hello I am satheesh"

uncommon = uncommon_words(string1, string2)
print("Uncommon words : ",uncommon)