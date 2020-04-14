# CODED BY SAM@SAMEER
# EMAIL:SAMS44802@GMAIL.COM
# DATE:06/03/2020
i = 0
number = int(input("TYPE THE NUMBER :"))
for  var in range(1,2000):
    if var**2 == number:
        print("NUMBER IS PERFECT SQUARE")
        i = 1
        break
    else:
        continue
if i == 0:
    print("NUMBER IS NOT PERFECT SQUARE")
else:
    pass