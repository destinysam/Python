# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 28/08/2019
# PROGRAM: PRINT A FIBONACCI SERIES


def fibonacci_series(number):
    a = 0
    b = 1
    if number == b:
        print(a)
    elif number == 2:
        print(a, b)
    else:
        print(a, b, end=" ")
        for i in range(number-2):
            c = a + b  # 1,2, 3,5,8
            a = b  # 1, 1, 2,3,5
            b = c  # 1, 2,3,5,8,
            print(b, end=" ")  # 1, 2, 3,5,8


number = int(input('ENTER THE NUMBER'))
fibonacci_series(number)