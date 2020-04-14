# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 30/08/2019
# PROGRAM: HOW TO USE APPEND FUNCTION IN LISTS
name = []  # LIST DECLARATION
student_rol = int(input('ENTER THE NUMBER OF STUDENTS :'))
i = 0
while i <= student_rol:
    student_name = input('ENTER THE NAME OF STUDENT :')
    name.append(student_name)  # ADDING STUDENT TO LIST
    i = i + 1
print(f"THE STUDENT_NAMES YOU ENTERED ARE :\n{name}")