#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:20/09/2019
#  PROGRAM: TO EXTRACT THE EMAIL FORM TEXT
import re
pattern = r"[\w.-]+@[\w.-]+"  # [\w,-]+ matches one or more occurrences of character(s),dot, or dash
text = input("TYPE TEXT INCLUDING EMAIL :")
match = re.search(pattern,text)
if match:
    print(f"EMAIL TO {match.group()}")
else:
    print("EMAIL NOT FOUND ")