# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 28/08/2019
# PROGRAM: TO FIND THE GREATEST OF THREE


def greater_num(a, b):
    if a > b:
        return a
    else:
        return b


def greatest_num(a, b, c):
    if a > b and a > c:
        return a
    else:
        if b > a and b > c:
            return b
        else:
            return c


def greatest_nu(x, y, z):
    greater = greater_num(x, y)
    greatest = greatest_num(greater, z)


print(f"GREATEST NUMBER IS: {greatest_num(56, 78, 44)}")