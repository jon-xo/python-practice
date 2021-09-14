# string_methods.py

## .upper(), .lower(), .title()
## String methods can only create new strings and will not change the original

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)

## .split()
## Split creates a list of strings based on spaces or the provided delimiter
line_one = "The sky has given over"
line_one_words = line_one.split()

## Split can also be used with a string to create a list of strings found
## around that string. If the character used appears at the end of the original string
## the list created will end with an empty string.

greatest_guitarist = "santana"
print(greatest_guitarist.split('n'))

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
author_last_names = [name.split()[-1] for name in author_names]
# print(author_names)
print(author_last_names)

## Additionally, Split can be used with escape sequences
## \n: Newline
## \t: Horizontal Tab

## .join()

## join is the opposite of split and uses a different syntax:
## 'delimiter'.join(list_you_want_to_join)


reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)

## join can also be used to with other strings and escapes as the delimiter

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

## .replace()

## .strip()
## strip allows for removing leading and trailing whitespace surronding strings.
## strip also will remove occurances of a string when passed as a parameter





## .format()
