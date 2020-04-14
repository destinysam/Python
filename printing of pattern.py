#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:12/09/2019
#  PROGRAM: PRINTING OF PATTERN


def pattern(character="%", r=1, n=6):
    for i in range(r):
        print()
    for j in range(n):
        print(character, end = ' ' " ")


character = input("ENTER THE ANY CHARACTER :")
rows = int(input("ENTER THE NO OF ROWS :"))
cols = int(input("ENTER THE NO OF COLUMNS :"))
pattern()
pattern(character, rows)
pattern(character, rows, cols)