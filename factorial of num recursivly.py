#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:12/09/2019
#  PROGRAM: FACTORIAL OF A NUMBER USING RECURSION


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)


number = int(input("ENTER THE NUMBER :"))
print(f"FACTORIAL OF {number}  IS {factorial(number)}")