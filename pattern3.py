#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:20/09/2019
rows = int(input("ENTER THE NO OF ROWS :"))
for i in range(1, rows+1):
    for j in range(1,i+1):
        print(" ",end='')
    index = rows
    while index >= 1:
        print(rows,end=' ')
        index -= 1
    rows -= 1
    print("\n")
