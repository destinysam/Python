#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:12/09/2019
#  PROGRAM:  SIMPLE CALCULATOR

import math  # PYTHON MODULE


def addition(a, b):  # FUNCTION DEFINITION
    a += b
    return a


def subtraction(a, b):
    a -= b
    return a


def multiplication(a, b):
    a *= b
    return a


def division(a, b):
    a /= b
    return a


def exponent(a):
    b = a ** 2
    return b


def square_root(a):
    b = math.sqrt(a)
    return b


print("\U0001F603")
print("HELLO I M YOUR SMART CALCULATOR")
print("TELL ME ANY MATH MATICAL OPERATION TO PERFORM")
while True:
    print("PLEASE CHOOSE FROM THE BELOW :")
    print("1.ADDITION\n 2.SUBTRACTION\n 3.MULTIPLICATION\n4.DIVISION\n5.EXPONENT\n6.SQUARE ROOT\n7.QUIT\n")
    choice = int(input("ENTER YOUR CHOICE"))
    if choice == 1:
        num1 = int(input("ENTER THE FIRST INTEGER NUMBER :"))
        num2 = int(input("ENTER THE SECOND INTEGER NUMBER  :"))
        print(addition(num1, num2))
    elif choice == 2:
          num1 = int(input("ENTER THE FIRST INTEGER NUMBER :"))
          num2 = int(input("ENTER THE SECOND INTEGER NUMBER  :"))
          print(subtraction(num1, num2))
    elif choice == 3:
          num1 = int(input("ENTER THE FIRST INTEGER NUMBER :"))
          num2 = int(input("ENTER THE SECOND INTEGER NUMBER  :"))
          print(multiplication(num1, num2))
    elif choice == 4:
          num1 = int(input("ENTER THE FIRST INTEGER NUMBER :"))
          num2 = int(input("ENTER THE SECOND INTEGER NUMBER  :"))
          print(division(num1, num2))
    elif choice == 5:
          num1 = int(input("ENTER THE INTEGER NUMBER :"))
          print(exponent(num1))
    elif choice == 6:
          num1 = int(input("ENTER THE INTEGER NUMBER  :"))
          print(square_root(num1))
    elif choice == 7:
        print("U CHOOSE EXIT BYE \U0001F608")
        break
    else:
        print("SORRY U ENTERED WRONG CHOICE")