#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:15/09/2019
#  PROGRAM: PRINTING OF TRIANGLE
character = input("ENTER THE CHARACTER :")
rows = int(input("ENTER THE ROWS :"))
for i in range(1, rows+1):
    for j in range(0, rows-i):
        print("", end=' ')
    for k in range(1,i+1):
        print(character,end=' ')
    print('\n')