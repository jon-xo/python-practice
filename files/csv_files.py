# csv_files.py
import csv

# Reference

big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 

# Print a CSV file to console

with open("users.csv") as users_csv_file:
    print(users_csv_file.read())

# Read a CSV file
# Using the open function with the newline argument to detect rows,
# combined with the csv libary's DictReader object, a new dictionary
# is created with keys matching the csv header row.

list_of_emails = []

with open('users.csv', newline='') as users_csv:
    user_reader = csv.DictReader(users_csv)
    for row in user_reader:
        list_of_emails.append(row['Email'])

print(list_of_emails)

# Read a delimiter-seperated CSV file

with open('address_book.csv', newline='') as addresses_csv:
    address_reader = csv.DictReader(addresses_csv, delimiter=';')
    for row in address_reader:
        print(row["Address"])


# Write to CSV file

csv_write = False

if csv_write == True:
    with open('output.csv', 'w') as output_csv:
        fields = ['name', 'userid', 'is_admin']
        output_writer = csv.DictWriter(output_csv, fieldnames=fields)

        output_writer.writeheader()
        for item in big_list:
            output_writer.writerow(item)

with open('output.csv') as output_csv:
    print(output_csv.read())