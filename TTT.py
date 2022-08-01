def TTT(score = [0, 0, 0]):
    moves = [str(i) for i in range(1, 10)]
    
    def show_board():
        print(moves[0] + '|' + moves[1] + '|' + moves[2])
        print('-----')
        print(moves[3] + '|' + moves[4] + '|' + moves[5])
        print('-----')
        print(moves[6] + '|' + moves[7] + '|' + moves[8])
        print()
    
    def move(player):
        move = ' '
        while not 48 < ord(move) < 58 or moves[int(move) - 1] != move:
            move = input("It is " + player + "'s move. Select an open position. ")
            if len(move) > 1:
                move = ' '
        moves[int(move) - 1] = player
        print()
    
    def check_win():
        if turn > 4 and moves[0] == moves[1] == moves[2] or \
           moves[3] == moves[4] == moves[5] or \
           moves[6] == moves[7] == moves[8] or \
           moves[0] == moves[3] == moves[6] or \
           moves[1] == moves[4] == moves[7] or \
           moves[2] == moves[5] == moves[8] or \
           moves[0] == moves[4] == moves[8] or \
           moves[2] == moves[4] == moves[6]:
            show_board()
            if turn % 2:
                print('X wins.')
                score[0] += 1
            else:
                print('O wins.')
                score[1] += 1
            return True
    
    for turn in range(1, 10):
        show_board()
        if turn % 2:
            move('X')
        else:
            move('O')
        if check_win():
            break

    else:
        show_board()
        print('The game is a draw.')
        score[2] += 1
    if input('Would you like to play again, (y)es or (n)o? ')[0].lower() == 'y':
        print()
        TTT(score)
    else:
        print('Final score:', score[0], 'win' if score[0] == 1 else 'wins', \
              'for X,', score[1], 'win' if score[1] == 1 else 'wins', 'for O,', score[2], 'draws.')
        
TTT()