# CODED BY SAM@SAMEER
# EMAIL:SAMS44802@GMAIL.COM
# DATE:23/03/2020
list1 = []
size_list = int(input("TYPE SIZE OF LIST :"))
for i in range(0,size_list):
    number = input("TYPE THE NUMBERS :")
    list1.append(int(number))
j=0
varieble = 0
for j in range(0,size_list-1):
    if list1[j] > list1[j+1]:
        varieble = list1[j]
        list1[j+1] = varieble
    elif list1[j] < list1[j+1]:
        varieble = list1[j+1]
    else:
        pass
print(f"{varieble}is the greatest no")