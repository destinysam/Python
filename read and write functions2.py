#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:23/09/2019
#  PROGRAM:TO WRITE AND READ THE FILE
file = open("file6.txt","r+")
print(file.read())
text = input("TYPE TEXT :")
file.write(text)