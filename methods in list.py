# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 31/08/2019
# PROGRAM: USING OF DIFFERENT FUNCTIONS IN LISTS
students = []  # LIST
student_rol = int(input('ENTER THE NUMBER OF STUDENTS :'))
i = 0
while i <= student_rol:
    student_name = input('ENTER THE NAME OF STUDENT :')
    students.append(student_name)
    i = i + 1
print(students)
students.sort()  # USING SORT FUNCTION TO SORT THE LIST
print(students)
print(sorted(students))  # TO SORT THE LIST
student_name = input('ENTER THE NAME OF STUDENT U WANT TO COUNT :')
print(students.count(student_name))  # USING COUNT FUNCTION TO COUNT THE ELEMENT IN THE LIST
student_copy = students.copy()   # USING COPY FUNCTION TO COPY THE LIST
print(student_copy)
students.reverse()  # USING REVERSE FUNCTION TO REVERSE THE LIST
print(students)
students.clear()
print(students)