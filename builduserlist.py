# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 5 /NOVEMBER/2019
# PROGRAM:  USER DEFINED LIST AND SOME FUNCTIONS


def make_list(lis):
    print(lis * 3)  # PRINTING USER DEFINED LIST MORE THAN ONE


lis = []
li = ["a",34,54,"b","coding"]
size = int(input("TYPE THE SIZE OF LIST :"))
for i in range(0, size):
    elements = input("TYPE ANY ELEMENT TO ADD TO THE LIST :")
    lis.append(elements)
lis += li

print(make_list(lis))