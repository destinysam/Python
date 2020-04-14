# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 27/08/2019
# PROGRAM: REVERSE OF STRING USING FUNCTIONS


def reverse_string(string_name):
    return string_name[::-1]


name = input('ENTER THE STRING NAME')
reverse = reverse_string(name)
print(reverse)


def string_character(string_name):
    return string_name[4]


name = input('ENTER THE STRING ')
character = string_character(name)
print(character)
