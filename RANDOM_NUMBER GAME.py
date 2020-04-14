# CODED BY SAM@SAMEER
# EMAIL: SAMS44802@GMAIL.COM
# DATE: 20/08/2019
# PROGRAM: NUMBER GUESSING GAME
winning_number = 50
number = int(input('ENTER THE NUMBER U WANT TO GUESS '))
game_over = False
guess = 0
while not game_over:
    if number == winning_number:
        print(f"U WIN, U GUESSED {guess} TIMES WRONG")
        game_over = True  # OR break
    else:
        if number >= winning_number:
            print('TOO HIGH')
            number = int(input('GUESS THE NUMBER AGAIN'))
            guess += 1
        else:
            print('TOO LOW')
            number = int(input('GUESS THE NUMBER AGAIN'))
            guess += 1



