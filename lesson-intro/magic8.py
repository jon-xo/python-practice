import random

# magic8.py answers yes / no questions with 
# one of 9 possible answers
#
# - "Yes - definitely."
# - "It is decidedly so."
# - "Without a dobut."
# - "Reply hazy, try again."
# - "Ask again later."
# - "Better not tell you now."
# - "My sources say no."
# - "Outlook not so good."
# - "Very dobutful."

name = input("Enter your name: ")
question = input("Input a yes or no question: ")
answer = ""

random_number = random.randint(1, 9)

# print(random_number)

# if/elif/else
if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a dobut."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very dobutful."
else:
    answer = "Error"

# Output:

if name:
    print()
    print(name + " asks: " + question)
else:
    print()
    print("Question: " + question)

if question:
    print()
    print("Magic 8-Ball's answer: " + answer)
else:
    print("Please enter a question to avoid a time/space fragment event.")

