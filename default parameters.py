# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 29/08/2019
# PROGRAM: WORKING OF DEFAULT PARAMETERS


def user_details(first_name="unknown", last_name="unknown", age=12):
    print(f"FIRST NAME IS :{first_name}")
    print(f"LAST NAME IS : {last_name}")
    print(f"AGE IS : {age}")


name = input('ENTER THE NAME OF USER :')
last_na = input('ENTER THE LAST NAME OF USER :')
age = input('ENTER THE AGE OF USER :')
user_details(name, last_na, age)