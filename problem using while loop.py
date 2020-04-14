# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 20/08/2019
# PROGRAM: TO SUM OF THE DIGITS OF A LONG INTEGER e,g 1234 =1+2+3+4 =10
number = input('ENTER ANY LONG  INTEGER NUMBER  ')
length = len(number)
i = 0
add = 0
while i < length:
     add = add + int(number[i])
     i = i + 1
print(add)