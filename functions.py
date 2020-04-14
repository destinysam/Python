# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 27/08/2019
# PROGRAM: USING OF FUNCTIONS
# TWO LINES SPACE BW COMMITS AND FUNCTION DEFINITION


def add_two(a, b):  # FUNCTION DEFINITION
    return a+b
# 2 LINES SPACE B/W THE FUNCTION DEFINITION AND FUNCTION CALL


total = add_two(5, 6)  # FUNCTION CALL
print(total)
#  print(add_two(5, 6))


def mul_two(x, y):  # FUNCTION DEFINITION
    return x*y


num1 = int(input('ENTER THE FIRST NUMBER'))
num2 = int(input('ENTER THE SECOND NUMBER'))
total = mul_two(num1, num2)  # FUNCTION CALL
print(total)


def add_string(first, last):
    return first + last


first_name = input('ENTER THE FIRST NAME :')
last_name = input('ENTER THE SECOND NAME :')
full_name = add_string(first_name, last_name)
print(full_name)



