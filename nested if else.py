# CODED BY SAM @SAMEER
# EMAIL:SAMS44802@GMAIL.COM
# DATE:19/10/2019
# PROGRAM: USING OF IF ELSE STATEMENTS IN PYTHON
name = "destinysam"
password = 1344
dob = 10_02_1999
friend_name = "faizan"
user_name = input("TYPE YOUR USER NAME :")
user_password = int(input("TYPE YOUR PASSWORD :"))
if user_name == name and user_password == password:
    print(f"THANK YOU {user_name}")
    print("U JUST COMPLETED FIRST LEVEL AUTHENTICATION")
else:
    print("\a")
    print("SORRY FIRST LEVEL AUTHENTICATION FAILED ")
    print("DUE TO INVALID PASSWORD OR USERNAME")
    exit(1)
date_of_birth = int(input("TYPE YOUR DATE OF BIRTH :"))
if date_of_birth == dob:
    print("SECOND LEVEL AUTHENTICATION COMPLETED ")
else:
    print("\a")
    print("FAILED: INVALID DATE OF BIRTH ")
    exit(1)
friend = input("TYPE YOUR CHILDHOOD FRIEND NAME :")
if friend == friend_name:
    print("U COMPLETED AUTHENTICATION")
    print("ACCESS GRANTED")
else:
    print("FAILED: INVALID FRIEND NAME")