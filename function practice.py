# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 28/08/2019
# PROGRAM: TO FIND THE GREATEST ONE


def greatest_num(a, b):
    if a > b:
        return a
    else:
        return b


num = int(input('ENTER THE FIRST NUMBER: '))
num1 = int(input('ENTER THE SECOND NUMBER: '))
greatest = greatest_num(num, num1)
print(f"GREATEST NUMBER IS: {greatest}")


