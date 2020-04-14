# CODED BY SAM @SAMEER
# EMAIL:SAMS44802@GMAIL.COM
# DATE: 20/10/2019
# PROGRAM: FINDING MAXIMUM AND MINIMUM NUMBER IN THE SERIES
numbers = []
size = int(input("TYPE THE SIZE OF THE LIST :"))
i = 0
while i < size:
    number = int(input(f"TYPE THE {i+1}  NUMBER :"))
    numbers.append(number)
    i += 1
for i in range(min(numbers)+1):
    if i in numbers:
        print(f"{i} IS SMALLEST NUMBER")
        break
    else:
        pass
i = max(numbers)
while i <= 0:
    if i in numbers:
        print(f" {i}  IS LARGEST NUMBER")
        break
    else:
        pass
