def reversed_string_list(siz, lis):
    reversed_list = []
    i = 0
    while i < siz:
        temp = reversed(lis[i])
        reversed_list.append(temp)
        i = i + 1
    return reversed_list


string_list = []
size = int(input("ENTER THE SIZE OF STRING LIST :"))
j = 0
while j < size:
    name = input(f"ENTER THE {j+1} STRING :")
    string_list.append(name)
    j = j + 1
print(reversed_string_list(size, string_list))