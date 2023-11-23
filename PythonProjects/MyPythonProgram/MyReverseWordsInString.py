from reverse_string import *

def reverse_words_in_string(mystring):


    # mystring = "python is good language"
    a = ""
    b = ""

    for i in mystring:

        if i != " ":
             a += i
        else:
            b = b + reverse_str(a) + " "
            a = ""
    b = b + reverse_str(a)   # to reveres last word if space is not after last word.
    # print(b)
    return b


string = "python is good language fun"
reversewords = reverse_words_in_string(string)
print(reversewords)
