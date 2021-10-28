# dictionary_challenge.py

# Sum values

def sum_values(my_dictionary):
    sum = 0
    for x in my_dictionary.values():
        sum += x
    return sum

print(sum_values({"milk":5, "eggs":2, "flour": 3}))

# Even keys

def sum_even_keys(my_dictionary):
    sum = 0
    for x in my_dictionary.keys():
        if x % 2 == 0:
            sum += my_dictionary[x]
    return sum

print(sum_even_keys({1:5, 2:2, 3:3}))

# Add Ten

def add_ten(my_dictionary):
    for x in my_dictionary.keys():
        my_dictionary[x] += 10
    return my_dictionary

# Values that are not keys

def values_that_are_keys(my_dictionary):
    my_list = []
    for x in my_dictionary.values():
        if x in my_dictionary:
            my_list.append(x)
    return my_list


# Largest value

def max_key(my_dictionary):
    m_key = 1
    a_key = 'a'
    for key in my_dictionary.keys():
        try:
            if my_dictionary[key] > my_dictionary[m_key]:
                m_key = key
        except KeyError:
            if my_dictionary[key] > my_dictionary[a_key]:
                m_key = key
    return m_key
    
print(max_key({1:100, 2:1, 3:4, 4:10}))
print(max_key({"a":100, "b":10, "c":1000}))

# Advanced

# Word length dict

def word_length_dictionary(words):
    new_dict = {}
    for w in words:
        new_dict[w] = len(w)
    return new_dict

print(word_length_dictionary(["apple", "dog", "cat"]))

# Frequency Count

def frequency_dictionary(words):
    new_dict = {}
    for w in words:
        if w in new_dict:
            new_dict[w] += 1
        else:
            new_dict[w] = 1
    return new_dict

print(frequency_dictionary(["apple", "apple", "cat", 1]))

print(frequency_dictionary([0,0,0,0,0]))

# Unique Values

def unique_values(my_dictionary):
    new_list = []
    for x in my_dictionary.values():
        if x not in new_list:
            new_list.append(x)
    return len(new_list)

print(unique_values({0:3, 1:1, 4:1, 5:3}))

# Count First Letter

def count_first_letter(names):
    letters = {}
    for l in names.keys():
        if l[0] not in letters.keys():            
            letters[l[0]] = 0        
            letters[l[0]] += len(names.get(l))
        else:
            letters[l[0]] += len(names.get(l))
    return letters

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))


# for player, words in player_to_words.items():
#     player_points = 0
#     for word in words:
#         player_points += score_word(word)
#     player_to_points[player] = player_points

 