#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:20/09/2019
rows = int(input("ENTER THE NUMBER OF ROWS :"))
for i in range(1, rows+1):
    for j in range(0,rows-i):
        print(" ",end='')
    for k in range(1,i+1):
        print(i,end=' ')
    print("\n")