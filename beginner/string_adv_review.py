# string_adv_review.py

# unique_english_letters takes a word as a parameter
# and returns the total number of unique characters,
# uppercase and lowercase characters should be counted
# indivually

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
    counter = 0
    for letter in letters:
        for char in word:
            compare_str = ""            
            if (len(compare_str) > 0):
                for sub in compare_str:
                    if(char != sub):
                        counter += 1
                        compare_str += char
                    else:
                        continue
            elif(char == letter):
                counter += 1
                compare_str += char
                break

    return counter


print(unique_english_letters("mississippi"))

# Count X

def count_char_x(word, x):
    count = 0
    for letter in word:
        if (letter == x):
            count += 1
    return count

print(count_char_x("mississippi", "m"))

# Count Multi X

def count_multi_char_x(word, x):
    occurances = word.split(x)
    return (len(occurances) - 1)

print(count_multi_char_x("Mississippi", "iss"))

# Substring Between

def substring_between_letters(word, start, end):
    if(word.find(start) != -1 and word.find(end) != -1):
        word_index = list(word)
        word_final = ""
        for i in range(len(word_index)):
            if (i > word.find(start) and i < word.find(end)):
                word_final += word_index[i]
        return word_final
    else:
        return word


print(substring_between_letters("apple", "p", "e"))

# X String

def x_length_words(sentence, x):
    sentence_list = sentence.split()
    for word in sentence_list:
        if (len(word) < x):
            return False
    return True

print(x_length_words("he like apples", 2))