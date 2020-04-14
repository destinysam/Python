# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 20/08/2019
# PROGRAM: WORD BUILDING GAME
name = "hold", "told", "gold", "count", "mount", "shown"
points = 0
print('**********WELCOME TO WORD BUILDING GAME********')
print('MODE:EASY\nLEVEL:1')
print("******[l,o,d,h]*******")
name = input('ENTER THE CORRECT WORD')
if name == "hold":
    points += 10
    print(f"U WIN {points} POINTS")
else:
    print(" U LOSE")
print('*******[t,d,o,l]*******')
name = input("ENTER THE CORRECT WORD")
if name == "told":
    points += 10
    print(f"U WIN {points} POINTS")
else:
    print("U LOSE")
print('*******[l,d,o,g]********')
name = input("ENTER THE CORRECT WORD")
if name == "gold":
    points += 10
    print(f"U WIN {points} POINTS")
else:
    print('U LOSE')
if points == 30:
    print(f"$$$CONGRATULATION$$$ U FINISHED THE FIRST LEVEL WITH {points} POINTS")
else:
    print(f"U HAVE EARN ONLY  {points} POINTS OUT OF 30 POINTS")
    print("U HAVE NOT COMPLETED THE FIRST LEVEL")
    print("***PLEASE COMPLETE THE FIRST LEVEL***")
    exit(1)
print("MODE:EASY\nLEVEL:2")
print("********[n,t,c,o,u]*********")
name = input('ENTER THE CORRECT WORD')
if name == "count":
    points += 10
    print(f"U WIN {points} POINTS")
else:
    print("U LOSE")
print("*******[m,u,o,t,n]*********")
name = input('ENTER THE CORRECT WORD')
if name == "mount":
    points += 10
    print(f"U WIN {points}  POINTS")
else:
    print("U LOSE")