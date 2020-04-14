# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 01/11/2019
# PROGRAM: CHECK WHETHER THE NUMBER IS PRIME OR NOT
from math import sqrt


def prime_no(num):
    trial_number = 2
    root = sqrt(num)
    while trial_number <= root:
        if num % trial_number == 0:
            return False
    return True


number = int(input("TYPE ANY NUMBER :"))
if prime_no(number):
    print(f"{number}  IS PRIME ")
else:
    print(f"{number} IS NOT PRIME")
