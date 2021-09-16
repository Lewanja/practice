# hello
#  h    e   l    l    o    w    o     r    l   d
#  0    0   1    2    2    2    2     2    3   3
def word(string, letter):
    # given string and a letter
    # have a variable called count to store the number of occurances of the letter
    occur=0
    # loop through all the letters in the string
    for character in string:

        # check if the letter of the string is same as the letter we are looking for
        if character == letter:
            occur +=1
            # if it it same we add one to count
        # if it not do nothing
        else:
            pass
    # get the total length of the string
    words=len(string)
    # return the result either fraction decimal depending on question
    return occur/words
s = input("Enter your string : ")
y=input("The letter is:")
x= word(s, y)
print(f"the value from this iteration is {x}")
