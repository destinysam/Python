# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 29/08/2019
# PROGRAM: SCOPE OF VARIABLES
x = 10  # GLOBAL VARIABLE
x = 9


def variable_scope():
    global x  # CHANGING GLOBAL TO LOCAL
    x = 5
    return x


print(variable_scope())
print(x)
print(x)