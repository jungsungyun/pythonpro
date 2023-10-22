import random


def instructions() :
    print("Welcome to the gretest intelletual challenge of all time: Tic-Tac-Toe.") 
    print("This will be a showdown between your human brain and my silicon processor.\n\n")
    print("You will make your move known by entering a number, 0 - 8. The number")
    print("will correspond to the board position as illstrated:\n")
    print("             0 : 1 : 2")
    print("             ---------")
    print("             3 : 4 : 5")
    print("             ---------")
    print("             6 : 7 : 8")
    print("Prepare yourself, human. The ultimate battle is about to begin.\n")

    
def pieces():
    human = input("Do you require the first move? <y/n>:")
    if human == 'y':
        return ('X','O')
    else:
        return ('O','X')
    
def new_board():
    return [' '] * 9
    
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    
def winner(board,player):
    ways_to_win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)] 
    for way in ways_to_win:
        if board[way[0]] == board[way[1]] == board[way[2]] == player:
            return True
    return False

def human_move(board, human):
    while True:
        move = ask_number("Where will you move?(0~8): ",0,9)
        print("Fine..")
        if board[move] == ' ':
            return move 
def computer_move(board, human, computer):
    legal_move = [i for i in range(9) if board[i] == ' ']
    return random.choice(legal_move)

def next_turn(turn):
    if turn == 'X':
        return 'O'
    else:
        return 'X'
def congrat_winner(the_winner, human,computer, turn):
    if the_winner == human:
        print(turn," won!\n")
        print("No,no! It cannot be! Somehow you tricked me. human.")
        print("But never again! I, the computer, so swears it!\n")
        print("Press the enter key to exit")
    elif the_winner == computer:
        print(turn," won!\n")
        print("As I predicted, human, I am triumphant once more.")
        print("Proof that computers are superior to humans in all regards.\n")
        print("Press the enter key to exit")
    else:
        print("draw") 
def ask_yes_no(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response
def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response    
def legal_moves(borad):
    return[i for i in range(9) if borad[i] == ' ']
    
def main():               
    instructions()
    human, computer = pieces()
    turn = 'X'
    board = new_board()
    
    while True:
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board,human,computer)
            board[move] = computer
            display_board(board)
            print("I Shall take square number",move)
        if winner(board, turn):
            congrat_winner(turn,human,computer,turn)
            break
        if ' ' not in board:
            print("draw")
            break
        turn = next_turn(turn)
main()
