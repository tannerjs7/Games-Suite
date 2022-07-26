from random import randint

def rps():
    print("Let's play Rock-Paper-Scissors.")
    choice = input('Select (r)ock, (p)aper, or (s)cissors: ')[0].lower()
    while choice != 'r' and choice != 'p' and choice != 's':
        choice = input('Please try again. Select (r)ock, (p)aper, or (s)cissors: ')[0].lower()
    rand = randint(1, 3)
    if rand == 1:
        opp = 'rock'
    elif rand == 2:
        opp = 'paper'
    else:
        opp = 'scissors'
    print('Your opponent chose ' + opp + '.')
    if choice == opp[0]:
        print('The game is a draw.')
    elif choice == 'r' and rand == 2 or choice == 'p' and rand == 3 or choice == 's' and rand == 1:
        print('Sorry, you lose.')
    else:
        print('Congratulations, you win.')
    if input('Would you like to play again: (y)es or (n)o? ')[0].lower() == 'y':
        print()
        rps()
        
rps()