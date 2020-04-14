# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 17/08/2019
# PROGRAM: USING OF REPLACE AND FIND FUNCTIONS
programmer = 'programmers of tomorrow are the wizards of future'
print(programmer.replace(" ", ""))  # REPLACING SPACES
# SYNTAX STRING_NAME.REPLACE("OLD", "NEW", POSITIONS)
print(programmer.replace("of", "are", 2))  # REPLACING 'OF' IN 2 POSITION
print(programmer.replace("are", "is", 1))   # REPLACING 'OF' IN 1 POSITION
print(programmer.find("of", 1))  # USING FIND FUNCTION TO FIND THE POSITION OF A STRING
programmer = "they find the access the technology or develop the software in very burdensome and complicated"
pos_the = programmer.find("the", 1)  # FINDING POSITION OF FIRST 'THE'
print(pos_the)
pos_the2 = programmer.find("the", pos_the+1)   # FINDING POSITION OF SECOND 'THE'
print(pos_the2)
pos_the3 = programmer.find("the", pos_the2+1)  # FINDING POSITION OF THIRD 'THE'
print(pos_the3)
