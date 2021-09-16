#given a string count the number of vowels
#input is string
#loop through the whole string
#have a variable that will count occurrences of vowels
#check for each letter if it is a, e, i, o, u
# check if the letter is in a list of vowels
#if it  is increment that variable
#return the variable

def word1(string):
    result=0
    vowels=set()
    for v in string:
        if v == 'a' or v =='e' or v=='i' or v=='o' or v=='u':
            result += 1
            vowels.add(v)
        else:
            pass
    return result, vowels


def word2(string):
    result=0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for v in string:
        if v in vowels:
            result += 1
        else:
            pass
    return result



x=input("write the string here:" )
y=word2(x)
print(y)