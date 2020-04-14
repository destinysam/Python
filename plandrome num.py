# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 28/08/2019
# PROGRAM: TO FIND A WORD OR NUMBER IS PALINDROME OR NOT


def palindrome_word(word):
    reverse = word[::-1]
    if word == reverse:
        print("WORD IS PALINDROME")
    else:
        print("WORD IS NOT PALINDROME")


word = input("ENTER THE SINGLE WORD oR ANY NUMBER :")
palindrome_word(word)