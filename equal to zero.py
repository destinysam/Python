# CODED BY SAM@SAMEER
# EMAIL:SAMS44802@GMAIL.COM
# DATE:22/03/2020
list1 = []
list2 = []
size_list = int(input("TYPE THE SIZE OF LIST"))
for i in range(0, size_list):
    number = input("TYPE THE NUMBERS")
    list1.append(int(number))
j = 0
while j < size_list:
    for i in list1:
        if list1[j]+i == 0:
            var = str(list1[j]) + "," +str(i)
            list2.append(var)
    j = j+1
print(list2)


