# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 31/08/2019
# PROGRAM: SQUARING OF LIST


def squaring_list(siz, lis):
    squared_list = []
    temp = 0
    counter = 0
    i = 0
    while i < siz:
        counter = int(lis[i])
        temp = counter ** 2
        squared_list.append(temp)
        i = i + 1
    return squared_list


number = []
size = int(input("ENTER THE SIZE OF LIST"))
j = 0
while j < size:
    num = input("ENTER THE ELEMENTS OF LIST :")
    number.append(num)
    j = j + 1
print(f"SQUARED LIST IS: \n {squaring_list(size, number)}")