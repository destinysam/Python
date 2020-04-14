#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:24/03/2020
list1 = []
duplicate_numbers = []
size_list = int(input("TYPE SIZE OF LIST :"))
for i in range(0,size_list):
    numbers = input("TYPE THE NUMBERS :")
    list1.append(numbers)
k = 1
for i in range(0,size_list-1):
    for j in range(k,size_list-k):
        if list1[i] == list1[j]:
            duplicate_numbers.append(list1[i])
    else:
        pass
    k += 1
print(duplicate_numbers)
for number in duplicate_numbers:
    if number in list1:
        list1.remove(number)
print(list1)