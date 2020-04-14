# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 28/08/2019
# PROGRAM: PROGRAM TO ADD THE DIGITS
name = input('ENTER THE NUMBER :')
total = 0
for i in name: # NEW WAY
    total += int(i)
print(total)
name = "sameer"
total = 0
for i in range(len(name)):  # OLD WAY
    total += int(i)
print(total)