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

winter_trees_full = '\n'.join(win59ter_trees_lines)
print(winter_trees_full)

## .replace()
## replace takes two arguments and replaces all instances of the first,
## with the second

with_spaces = "You got the kind of loving that can be so smooth"

with_underscores = with_spaces.replace(' ', '_')
print(with_underscores)

## .strip()
## strip allows for removing leading and trailing whitespace surronding strings.
## strip also will remove occurances of a string when passed as a parameter

featuring = "           rob thomas                 "
print(featuring.strip())

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

# love_maybe_lines_stripped = [line.split('') if line == '' else line.strip() for line in love_maybe_lines]
# love_maybe_full = ' '.join([line.split('') for line in love_maybe_lines_stripped])

love_maybe_lines_stripped = []

for line in love_maybe_lines:
    if line == '\n':
        love_maybe_lines.remove(line)
    else:
        love_maybe_lines_stripped.append(line.strip())

print(love_maybe_lines_stripped)
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

## .find()
## find method accepts a single argument and returns the first 
## matching index value of a matching string
print('smooth'.find('t'))

## .format()
## the format method facilitates variable string replacement. 
## {} is used a placeholder for the variable passed to format

def favorite_movie_string(movie, director):
    return "My favorite movie is \"{movie}\" by {director}.".format(movie=movie, director=director)

print(favorite_movie_string("Star Wars", "George Lucas"))

def poem_title_card(title, poet):
    return "The poem \"{}\" is written by {}.".format(title, poet)
