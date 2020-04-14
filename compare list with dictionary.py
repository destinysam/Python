# CODED BY SAM@SAMEER
# EMAIL:SAMS44802@GMAIL.COM
# DATE:05/12/2019
# PROGRAM:
lis = []
for i in range(1,11):
    lis.append(i)
print(lis)
dictionary_nam = {}
for j in lis:
    dictionary_nam[j] = j
print(dictionary_nam)
dictionary_nam[12] = 12
print(dictionary_nam)
p_position = int(input("TYPE THE POSITION NAME WHERE U WANT TO INSERT NUMBER :"))
i_number = int(input("TYPE THE NUMBER U WANT TO INSERT :"))
lis.insert(p_position,i_number)
print(lis)
for i in lis:
    if i in dictionary_nam.keys():
        continue
    else:
        print(i)
for i in dictionary_nam.keys():
    if i in lis:
        continue
    else:
        print(i)