# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 31/08/2019
# PROGRAM: CHANGING OF POSITIVE LIST INTO NEGATIVE LIST
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def negative_fun(lis):
    negative = []
    for i in lis:
        negative.append(-i)
    return negative


print(negative_fun(number))


