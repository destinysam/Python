#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:26/09/2019


class Human:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def running(self):
        print(f"{name} IS MY NAME")
        print(f"{age} IS MY AGE")
        print(f"{address} IS MY ADDRESS")


name = input("TYPE NAME :")
age = int(input("TYPE AGE"))
address = input('TYPE ADDRESS')
person = Human(name,age,address)
person.running()