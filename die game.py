# CODED BY SAM @SAMEER
# EMAIL:SAMS44802@GMAIL.COM
# DATE: 21/10/2019
# PROGRAM: DIE THROWN GAME
from random import randrange  # MODULE
player1 = player2 = 0
die_thrown = int(input("TYPE HOW MANY TIMES U WANT TO THROW THE DIE 'EVEN NOS ONLY' :"))
print("****THIS GAME HAS TWO PLAYERS****")
print("******ONE WHO THROW THE DIE FIRST IS PLAYER A******")
print("**SECOND DIE THROWER IS PLAYER B")
for i in range(1,die_thrown+1):
    choice = input("PLEASE TYPE YOUR PLAYER NAME a or b 'only lower case allowed':")
    number = randrange(1,6) # randrange is imported function that gives random no for every  call
    print("+-----+")
    if number == 1:
        print("|    |")
        print("|  * |")
        print("|    |")
        if choice == 'a':
            player1 += 1
        else:
            player2 += 1
        continue
    elif number == 2:
        print("|*   |")
        print("|    |")
        print("|   *|")
        if choice == 'a':
            player1 += 2
        else:
            player2 += 2
        continue
    elif number == 3:
        print("|*   |")
        print("|  * |")
        print("|   *|")
        if choice == 'a':
            player1 += 3
        else:
            player2 += 3
        continue
    elif number == 4:
        print("|*  *|")
        print("|    |")
        print("|*  *|")
        if choice == 'a':
            player1 += 4
        else:
            player2 += 4
        continue
    elif number == 5:
        print("|*  *|")
        print("|  * |")
        print("|*  *|")
        if choice == 'a':
            player1 += 5
        else:
            player2 += 5
        continue
    elif number == 6:
        print("|*  *|")
        print("|*  *|")
        print("|*  *|")
        if choice == 'a':
            player1 += 6
        else:
            player2 += 6
        continue
    else:
        print("INVALID DIE THROWN ")
print(f"PLAYER A HAVE WON {player1} POINTS")
print(f"PLAYER B HAVE WON {player2} POINTS")

