# CODED BY SAM@SAMEER
# EMAIL:SAMS44802@GMAIL.COM
# DATE:05/12/2019
dictionary_num = {}
size = int(input("TYPE HOW MANY ELEMENTS U WANT TO INSERT :"))
for i in range(size):
    key_name = int(input("TYPE THE KEY NAME :"))
    dictionary_num[key_name] = "student" + str(key_name)
print(dictionary_num)

