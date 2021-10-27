# string_challenge.py

# Check name

def check_for_name(sentence, name):
    if name.lower() in sentence.lower():
        return True
    else:
        return False
        
print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))

# Every other letter

def every_other_letter(word):
    final = ""
    for x in range(0, len(word), 2):
        final += word[x]
    return final

print(every_other_letter("Codecademy"))

# Reverse

def reverse_string(word):
    final = ''
    for x in range(len(word)-1, -1, -1):
            final += word[x]
    return final

print(reverse_string("Codecademy"))

# Spoonerism

def make_spoonerism(word1, word2):
    l1 = word1[0]
    l2 = word2[0]
    return l2 + word1[1:] + " " + l1 + word2[1: ]

print(make_spoonerism("Hello", "world"))

# Add Exclamation

def add_exclamation(word):
    if len(word) >= 20:
        return word
    else:
        for x in range(20):
            word += "!"
            if len(word) == 20:
                return word

print(add_exclamation("Codecademy"))
print(add_exclamation("Codecademy is the best place to learn"))

