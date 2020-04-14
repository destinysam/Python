#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:27/09/2019
import random
list1 =[1,2,4,5,6,7,8,9,12,45]
#size_list = int(input('TYPE SIZE OF LIST :'))
#for i in range(0,size_list):
#    number = input('TYPE THE NUMBER')
#    list1.append(number)




class die:
    def __init__(self,list1):
        self.list1 = list1

    def roll_die(self):
        variable = random.choices(list1,weights=None,cum_weights=None,k=2)
        return variable



obj1 = die(list1)
print(obj1.roll_die())

