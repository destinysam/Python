#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:15/09/2019
#  PROGRAM:TO FIND THE LEAP YEAR
year = int(input("ENTER THE YEAR WHERE U WANT TO START TO FIND LEAP YEAR :"))
year1 = int(input("ENTER THE RANGE OF YEAR :"))
for i in range(year,year1):
    if i % 4 == 0:
        print(f"{i} IS LEAP YEAR ")
