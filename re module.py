#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:19/09/2019
import re
message = input("TYPE YOUR MESSAGE :")
word = input("TYPE WHICH WORD U WANT TO FIND :")
if re.search(word,message):
    print(f"{word} WORD FOUND")
else:
    print(f"{word} NOT FOUND")
