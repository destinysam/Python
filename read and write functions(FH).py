#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:22/09/2019
#  PROGRAM: TO WRITE AND READ THE FILE CONTENT
file = open("file3.txt", "r+")
file.write("HELLO WELCOME TO PYTHON WORLD")
print(file.read(29))
file.close()