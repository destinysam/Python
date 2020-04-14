number = []
size = int(input("ENTER THE SIZE OF LIST :"))
j = 0
while j < size:
    num = int(input(f"ENTER THE {j+1} NUMBERS :"))
    number.append(num)
    j = j + 1
for i in set(number):
    print(i)
