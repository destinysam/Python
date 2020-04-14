# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 20/08/2019
# PROGRAM: PROGRAM TO FIND THE GRADE OF A STUDENT BY ADDING THE MARKS OF ALL SUBJECTS
name = input('ENTER THE NAME OF STUDENT ')
roll_no = int(input("ENTER THE ROLL NO OF STUDENT "))
subject1 = int(input('ENTER THE MARKS OF SCIENCE SUBJECT '))
subject2 = int(input('ENTER THE MARKS OF MATH SUBJECT '))
subject3 = int(input('ENTER THE MARKS OF COMPUTER SUBJECT '))
subject4 = int(input('ENTER THE MARKS OF  ENGLISH SUBJECT '))
subject5 = int(input('ENTER THE MARKS OF SOCIAL SCIENCE SUBJECT '))
total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks/500) * 100
if percentage >= 90.0:
    print(f'{name} HAS A++ GRADE')
else:
    if percentage >= 80.0:
        print(f'{name} HAS GOT A+ GRADE')
    else:
        if percentage >= 70.0:
            print(f"{name} HAS GOT A GRADE ")
        else:
            if percentage >= 60.0:
                print(f"{name} HAS GOT B GRADE ")
            else:
                if percentage >= 50.0:
                    print(f"{name}  IS PASS WITH C GRADE")
                else:
                    if percentage >= 40.0:
                        print(f"{name} IS PASS WITH D GRADE")
                    else:
                        print('FAIL')


