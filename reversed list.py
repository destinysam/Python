# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 31/08/2019
# PROGRAM: TO REVERSE THE LIST


def reversed_list(siz, lis):
    rev = []
    j = siz-1
    while j >= 0:
        temp = lis[j]
        rev.append(temp)
        j = j-1
    return rev
#   ALTERNATIVE return lis[::-1]


number = []
size = int(input("ENTER THE SIZE OF LIST"))
i = 0
while i < size:
    num = input("ENTER THE NUMBERS OF THE LIST :")
    number.append(num)
    i = i + 1
print(f"REVERSED LIST IS: \n {reversed_list(size, number)}")

