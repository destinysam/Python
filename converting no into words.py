#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:26/09/2019
dictionary = {}
d = {}
size_dict = int(input("TYPE THE SIZE :"))
for i in range(0,size_dict):
    keys = input(f"TYPE THE {i+1} KEY OF THE LIST:")
    value = input("TYPE VALUE :")
    dictionary[keys] = value
print(dictionary)
dictionary.pop('name')
print(dictionary)
