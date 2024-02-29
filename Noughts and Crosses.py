SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, EMPTY = 'X', 'O', ' '  # Markers for players and empty spaces.

def play_game():
    print('Noughts and Crosses')
    board = new_board()  # Initialises game board to be blank .
    current, next_player = X, O  # Set X to go first.

    while True:  # Game loop.
        print(board_to_string(board))

        # Ask for a move until it's valid.
        move = None
        while not valid_move(board, move):
            print(f"{current}'s turn to move: (1-9)")
            move = input('> ')
        make_move(board, move, current)  # Update the board.

        # Check for win or tie.
        if winner(board, current):
            print(board_to_string(board))
            print(f'{current} wins!')
            break
        elif full_board(board):
            print(board_to_string(board))
            print('It\'s a tie!')
            break
        current, next_player = next_player, current  # Switch turns.
    print('Thanks for playing!')

def new_board():
    """Make a new blank board."""
    return {space: EMPTY for space in SPACES}

def board_to_string(board):
    """Turn the board into a string to print."""
    return '''
      {}|{}|{}  
      -+-+-
      {}|{}|{}  
      -+-+-
      {}|{}|{}  '''.format(board['1'], board['2'], board['3'],
                           board['4'], board['5'], board['6'],
                           board['7'], board['8'], board['9'])

def valid_move(board, move):
    """Check if a move is valid (in the list and on an empty space)."""
    return move in SPACES and board[move] == EMPTY

def winner(board, player):
    """Check if the player has won."""
    b, p = board, player
    return ((b['1'] == b['2'] == b['3'] == p) or
            (b['4'] == b['5'] == b['6'] == p) or
            (b['7'] == b['8'] == b['9'] == p) or
            (b['1'] == b['4'] == b['7'] == p) or
            (b['2'] == b['5'] == b['8'] == p) or
            (b['3'] == b['6'] == b['9'] == p) or
            (b['3'] == b['5'] == b['7'] == p) or
            (b['1'] == b['5'] == b['9'] == p))

def full_board(board):
    """Check if the board is full."""
    return all(board[space] != EMPTY for space in SPACES)

def make_move(board, space, mark):
    """Update the board with a player's mark."""
    board[space] = mark

if __name__ == '__main__':
    play_game()  # Start the game if this script is run directly.