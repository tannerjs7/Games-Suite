def connect_4(score = [0, 0]):
    
    board = [['o'] * 7 for _ in range(6)]
    black_wins = red_wins = False
        
    def print_board():
        for row in board:
            print(row)
            
    def get_move():
        if move_num % 2:
            print("It is black's move.")
        else:
            print("It is red's move.")
        col = 9
        while col == 9:
            col = input('Select a column from 1 to 7: ')
            if len(col) == 1 and 49 <= ord(col) <= 55:
                col = int(col) - 1
                if board[0][col] != 'o':
                    col = 9
                    print('That column is full. Try another.')
            else:
                col = 9
        print()
        return col
    
    def make_move():
        for i in range(5, -1, -1):
            if board[i][col] == 'o':
                board[i][col] = 'B' if move_num % 2 else 'R'
                return i
            
    def check_for_win():
        if move_num >= 7:
            if move_num % 2:
                if 'BBBB' in ''.join(board[row][0:7]) or \
                    'BBBB' in ''.join([x[col] for x in board]) or \
                    'BBBB' in ''.join([board[x + row - col][x] for x in range(7) if 0 <= x + row - col <= 5]) or \
                    'BBBB' in ''.join([board[row + col - x][x] for x in range(7) if 0 <= row + col - x <= 5]):
                    nonlocal black_wins
                    black_wins = True
                    score[0] += 1
                    return True
            elif 'RRRR' in ''.join(board[row][0:7]) or \
                'RRRR' in ''.join([x[col] for x in board]) or \
                'RRRR' in ''.join([board[x + row - col][x] for x in range(7) if 0 <= x + row - col <= 5]) or \
                'RRRR' in ''.join([board[row + col - x][x] for x in range(7) if 0 <= row + col - x <= 5]):
                nonlocal red_wins
                red_wins = True
                score[1] += 1
                return True
            
    def announce_result():
        print_board()
        if black_wins:
            print('Connect Four!')
            print('Black wins in', move_num, 'moves.')
        elif red_wins:
            print('Connect Four!')
            print('Red wins in', move_num, 'moves.')
        else:
            print('The game is a draw.')
        if input('Would you like to play again, (y)es or (n)o? ')[0].lower() == 'y':
            print()
            connect_4(score)
        else:
            print('Final score:', score[0], 'win' if score[0] == 1 else 'wins', 'for black,', \
                  score[1], 'win' if score[1] == 1 else 'wins', 'for red')
    
    for move_num in range(1, 43):
        print_board()
        col = get_move()
        row = make_move()
        if check_for_win():
            break
    announce_result()
    
connect_4()