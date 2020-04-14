# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 30/08/2019
# PROGRAM: USING OF MORE METHODS TO ADD DATA TO LIST
name = []  # LIST DECLARATION
student_rol = int(input('ENTER THE NUMBER OF STUDENTS :'))
i = 0
while i <= student_rol:
    student_name = input('ENTER THE NAME OF STUDENT :')
    name.append(student_name)  # ADDING STUDENT TO LIST
    i = i + 1
print(f"THE STUDENT_NAMES YOU ENTERED ARE :\n{name}")
print("PRESS 1 IF U FORGET ANY STUDENT NAME ELSE PRESS 0")
press = int(input('ENTER YOUR CHOICE :'))
if press == 1:
    student_name = input('ENTER THE NAME OF STUDENT U FORGET :')
    name.insert(3, student_name)  # USING INSERT TO ADD DATA TO LIST AT PARTICULAR POSITION
else:
    pass
print(f"THE STUDENT_NAMES YOU ENTERED ARE :\n{name}")
colleges = []
i = 0
while i <= student_rol:
    college_name = input('ENTER THE COLLEGE NAMES OF ENTERED STUDENT')
    colleges.append(college_name)
    i = i + 1
print(f"THE COLLEGES OF ENTERED STUDENTS ARE :\n{colleges}")
student_details = name + colleges
print(student_details)
name.extend(colleges)  # USING EXTEND TO COMBINE THE TWO LISTS
print(name)
name.append(colleges)  # USING APPEND TO ADD THE ALL LIST
print(name)