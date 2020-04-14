#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:26/09/2019

list1 = []
not_twice = []
size_list = int(input('TYPE SIZE :'))
for i in range(0,size_list):
    number = input('TYPE ELEMENTS OF LIST :')
    list1.append(int(number))
k =1
for lis in range(0,size_list):
    for i in range(k,size_list):
        if list1[lis] == list1[i]:
            not_twice.append(list1[i])
        else:
            pass
    k += 1
print(f'{not_twice} ELEMENTS THAT ARE APPEARED TWICE')

