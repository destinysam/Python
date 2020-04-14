#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:19/09/2019
#  PROGRAM:HOW TO ENCRYPT A MESSAGE
message = input("TYPE YOUR MESSAGE :")
i = 0
while i < len(message):
    message1 = message[i]
    if message1 >= 'm' or 'M':
        print(chr(ord(message1)+5),  end=' ')
    else:
        print(chr(ord(message1)+3), end=' ')
    i += 1