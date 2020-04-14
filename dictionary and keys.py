# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 02/09/2019
# PROGRAM: DICTIONARY AND ITS FUNCTIONS
dictionary = {1, 4, 5, 6, "sameer"}
print(dictionary)
dictionary = {"NAME ": "SAMEER", "ADDRESS ": "TARIGAM", "AGE ": "21"}
print(dictionary.keys())
print(dictionary.values())
print(dictionary.copy())
print(dictionary.items())
del dictionary["NAME "]
print(dictionary)
dictionary["NAME"] = "SAMEER"
print(dictionary)
for i in dictionary.items():
    print(i)
print(dictionary.__sizeof__())

