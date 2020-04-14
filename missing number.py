# CODED BY SAM@SAMEER
# EMAIL:SAMS44802@GMAIL.COM
# DATE:06/03/2020
input_numbers = []
missing_numbers = []
num = int(input("TYPE THE SIZE OF NUMBERS"))
for i in range(0,num):
    var = input("TYPE THE NUMBERS")
    input_numbers.append(var)
temp = int(input_numbers[0])
for j in range(0,num):
    if temp == int(input_numbers[j]):
        pass
    else:
        print(f"{temp} NOT FOUND")
        break
       #missing_numbers.append(temp)
       j -= 1
    temp += 1
#for  k in missing_numbers:
 #   print(k)