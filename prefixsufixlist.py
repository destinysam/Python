# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 05/NOVEMBER/2019
# PROGRAM: PRINTING LIST IN A PREFIX AND SUFFIX STRUCTURE
list = [1,2,3,4,5,6]
print("****A LIST IN A PREFIX STRUCTURE****")
for i in range(0,len(list)+1):
    print(list[0:i])
print("************************************")
print("A LIST IN A SUFFIX STRUCTURE")
for i in range(len(list), -1, -1):
    print(list[0:i])
