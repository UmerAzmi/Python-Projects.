import random

print('Welcome to Tic Tac Toe.')

board = [' ' for _ in range(9)]

def show_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def check_winner(player):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_board_full():
    return ' ' not in board

def user_move():
    while True:
        try:
            move = int(input('Choose position (1-9): ')) - 1
            if move < 0 or move > 8:
                print('Choose between 1 and 9.')
            elif board[move] != ' ':
                print('Position already taken.')
            else:
                board[move] = 'X'
                break
        except:
            print('Please enter a number.')

def computer_move():
    print('Computer is thinking...')

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner('O'):
                return
            board[i] = ' '

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner('X'):
                board[i] = 'O'
                return
            board[i] = ' '

    available_moves = [i for i in range(9) if board[i] == ' ']
    move = random.choice(available_moves)
    board[move] = 'O'

print('\nYou are X')
print('Computer is O')
show_board()

while True:
    user_move()
    show_board()

    if check_winner('X'):
        print('You won! 🎉')
        break

    if is_board_full():
        print('It\'s a draw!')
        break

    computer_move()
    show_board()

    if check_winner('O'):
        print('Computer won!')
        break

    if is_board_full():
        print('It\'s a draw!')
        break
