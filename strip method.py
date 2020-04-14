# CODED BY SAM@SAMEER
# EMAIL: SAMS44902@GMAIL.COM
# DATE: 17/08/2019
# PROGRAM: USING STRIP METHOD TO ELIMINATE THE SPACES AROUND THE STRING
name = "     programming is source of creativity     "
language = " python"
print(name.lstrip())  # ELIMINATE ONLY LEFT SPACES OF A GIVEN STRING
print(name.rstrip() + language)  # ELIMINATE ONLY RIGHT SPACES OF A GIVEN STRING
print(name.strip() + language)  # ELIMINATE BOTH RIGHT AND LEFT SPACES
print(name.replace(" ", ""))  # USING REPLACE FUNCTION TO REDUCE THE SPACE B/W  STRINGS
name = input('ENTER YOUR NAME ')
print(name.strip())
print(name.strip().lower().count("g"))
