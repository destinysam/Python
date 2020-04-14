# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 31/08/2019
# PROGRAM: COMPARING OF is AND ==
students = []  # LIST DECLARATIONS
student_rol = int(input('ENTER THE NUMBER OF STUDENTS :'))
i = 0
while i <= student_rol:
    student_name = input('ENTER THE NAME OF STUDENT :')
    students.append(student_name)
    i = i + 1
student_copy = students.copy()
if student_copy == students:
    print("LISTS ARE EQUAL")
else:
    print("NOT EQUAL ")
print(student_copy == students)  # == IS USED TO CHECK THE VALUES ARE SAME OR NOT
print(student_copy is students)  # is IS USED TO CHECK WHEATHER THE LISTS ARE STORED AT SAME PLACE OR NOT
print(students)