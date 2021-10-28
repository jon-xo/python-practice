# files.py

# with keyword operates as a context manager, which controls opening
# and closing the file block, there for, all file operations happen
# in the indented block

# To read a file

with open('new_document.txt') as new_doc:
    doc_contents = new_doc.read()
print(doc_contents)

# iterate through lines of a file

with open('keats_poem.txt') as keats_poem:
    for line in keats_poem.readlines():
        print(line)

# read a specific line
# the readline method will read each line in sequence
# and return an empty string once the file is complete

with open('millay_sonnet.txt') as sonnet_doc:
    first_line = sonnet_doc.readline()
    second_line = sonnet_doc.readline()
    print(second_line)

# write to a file
# using the open function with an additional 'w' argument
# allows for write-only mode. This will create a new file with the 
# argument passed using the write method
# 
# !! If the file already exisits in the active directory,
# it will be over written

with open('write_file.txt', 'w') as write_file:
    write_file.write("Python script update!")

# append an existing file
# using the open function with an additional 'a' argument
# places the file in append mode, this will continue to modify
# the file every time the script is executed

with open('write_file.txt', 'a') as write_file:
    write_file.write("...Python script *appending* file")

