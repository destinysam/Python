#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:15/09/2019
#  PROGRAM: USING lambda FUNCTION TO ADD THE INTEGERS

num1 = int(input("ENTER THE NUMBER :"))
num2 = int(input("ENTER THE SECOND NUMBER :"))
add = lambda num1, num2: num1 + num2
print(add(num1, num2))
if num1 > num2:
    print("FIRST NUMBER IS GREATER")
else:
    print("SECOND NUMBER IS GREATER")
