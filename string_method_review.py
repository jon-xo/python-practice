# string_method_review.py

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"


highlighted_poems_list = highlighted_poems.split(",")

print(highlighted_poems_list)

highlighted_poems_stripped = [poem.strip() for poem in highlighted_poems_list]
print(highlighted_poems_stripped)

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
    highlighted_poems_details.append(poem.split(":"))

print(highlighted_poems_details)

titles = []
poets = []
dates = []

for poem_string in highlighted_poems_details:
    titles.append(poem_string[0])
    poets.append(poem_string[1])
    dates.append(poem_string[2])

## mark for reviewed

for i in range(len(titles) - 1):
    # print(titles[i])
    # print(poets[i])
    # print(dates[i])
    print("The poem {title} was published by {poet} in {date}.").format(title=titles[i], poet=poets[i], date=dates[i])