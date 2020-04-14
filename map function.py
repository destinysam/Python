#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:11/09/2019
#  PROGRAM: CONVERTING OF LIST NUMBERS INTO NEGATIVE NUMBERS


def negative(numbers, rang):
    return_list = []
    temp = 0
    counter = 0
    for j in range(rang):
        counter = int(numbers[j])
        temp = counter * -1
        return_list.append(temp)
    return return_list


number = []
size = int(input("ENTER THE SIZE OF LIST :"))
for i in range(size):
    num = input("ENTER THE NUMBERS OF THE LIST ")
    number.append(num)
print(negative(number, size))
