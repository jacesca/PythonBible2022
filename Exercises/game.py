# Tic Tac Toe
import random

board, stop = [], False
guest_icon, house_icon = 'X', 'O'

def print_board():
    print("| {} | {} | {} |".format(*board[0:3]))
    print("| {} | {} | {} |".format(*board[3:6]))
    print("| {} | {} | {} |".format(*board[6:]))
    print()

def restart_board():
    global board
    board, stop = [' ' for i in range(9)], False
    print_board()
    
def win_validate(icon):
    return (
        (board[0]==board[1]==board[2]==icon) or \
        (board[3]==board[4]==board[5]==icon) or \
        (board[6]==board[7]==board[8]==icon) or \
        (board[0]==board[3]==board[6]==icon) or \
        (board[1]==board[4]==board[7]==icon) or \
        (board[2]==board[5]==board[8]==icon) or \
        (board[0]==board[4]==board[7]==icon) or \
        (board[2]==board[4]==board[6]==icon)
    )

def player_move(icon):
    choice = input('Enter your move (1-9): ').strip().lower()
    if choice in ['q', 'n']:
        return choice
    elif choice.isdigit():
        choice = int(choice)
        if choice in range(1,10):
            if board[choice-1]==' ':
                board[choice-1]='X'
                return True
            else:
                print('That space is taken!')

def house_move(icon):
    available_choices = [i for i, x in enumerate(board) if x==' ']
    board[random.choice(available_choices)] = 'O'

def is_draw():
    return (' ' not in board)
    
print("""
Note:
q to quit
n to restart
""")

restart_board()
while True:
    choice = player_move(guest_icon)
    if choice=='q':
        break;
    elif choice=='n':
        restart_board()
    elif choice:
        if win_validate('X'):
            print('You win! Congratulations!')
            stop = True
        else:
            if is_draw():
                print('Game over! No body win!')
                stop = True
            else:
                house_move(house_icon)
                if win_validate('O'):
                    print('House win!')
                    stop = True
        print_board()
        if stop:
            print("\nLet's play again")
            restart_board()
    else:
        continue
