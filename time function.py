# CODED BY SAM @SAMEER
# EMAIL:SAMS44802@GMAIL.COM
# DATE: 21/10/2019
# PROGRAM: USING CLOCK FUNCTION TO FIND THE EXECUTION TIME OF PROGRAM
from time import clock
sum = 0
start_time = clock()
for i in range(1,10000001):
    sum+= i
print(f"YOUR SUM IS {sum}")
print(f"YOUR EXECUTION TIME IS {clock() - start_time} SECONDS")