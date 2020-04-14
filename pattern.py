#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:12/09/2019
#  PROGRAM: PRINTING OF TRIANGLE
character = input("ENTER THE CHARACTER :")
rows = int(input("ENTER THE NO OF ROWS :"))
for i in range(1, rows+1):
    print(character)
    for j in range(1, i+1):
        print(character, end=' ')
print(character)