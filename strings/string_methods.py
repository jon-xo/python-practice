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

## .replace()

## .strip()

## .format()