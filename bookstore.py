"""
You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including the space).

You are provided a books.txt file, which includes the book titles, each one written on a separate line.
Read the title one by one and output the code for each book on a separate line.

For example, if the books.txt file contains:
Some book
Another book

Your program should output:
S9
A12
"""

# algo : generate the code
# given a book name
# get the first letter
# get the number of charecter - length
# combine the two and return result

def generate_code(book_name):
    book_name = book_name.replace("\n", "")
    x=book_name[0]
    length=len(book_name)
    z= x+ str(length)
    return z

# algo 2 : get file contents
def read_file(file_name):
    with open(file_name, "r") as f:
        lines=f.readlines()
        return lines

# algo 3
# from the list of file contents
# loop through every line
booknames= read_file('books.txt')
for line in booknames:
    code = generate_code(line)
    print(code)
# generate the code for each line
# output the result
