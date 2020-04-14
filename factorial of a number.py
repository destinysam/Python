# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 31/10/2019
# PROGRAM: FIND THE FACTORIAL OF A NUMBER


def factorial_number(number):
    product = 1
    while number > 0:
        sum = number * product
        number -= 1
    print(f"FACTORIAL OF A NUMBER IS {product}")


number = int(input("TYPE ANY NUMBER "))
factorial_number(number)