# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 17/08/2019
# PROGRAM: USING CENTER METHOD TO ADD CHARACTERS TO STRING TO BOTH SIDES
name = "programming language"
length = len(name)
# SYNTAX STRING_NAME.CENTER(LENGTH+HOW MANY CHARACTERS WE WANT TO ADD, 'CHARACTER')
print(name.center(length+6, "*"))
name = input('ENTER THE NAME')
print(name.center(len(name)+6, "#"))