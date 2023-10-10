import random
board=["-","-","-",
        "-","-","-",
        "-","-","-"]

is_continue=True
player="X"
winner=None 
def print_board(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-----")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-----")
    print(board[6]+"|"+board[7]+"|"+board[8])
print_board(board)

def player_input(board):
    global player
    inp=int(input("Enter a number btween 1-9:"))
    if inp>=1 and inp<=9 and board[inp-1]=="-":
        board[inp-1]="X"
        
def check_horizantal(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner=board[3]
        return True    
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner=board[6]
        return True




def check_row(board):
    global winner   
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[0]
        return True

    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner=board[0]
        return True


def checkdiag(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[8] and board[2]!="-":
        winner=board[2]
        return True
def check_for_tie(board):
    if "-" not in board:
        print_board(board)
        print("It s tie!")
        is_continue=False                                 
def checkwin():
    if check_horizantal(board) or check_for_tie(board) or check_row(board) or checkdiag(board):
        print(f"The winner is {winner}")
def switch_player():
    global player
    if player=="X":
        player="O"
    else:
        player="X"    


def computer(board): 
    pos=random.randint(0,8)
    if board[pos]=="-":
        board[pos]="O"
        switch_player()


while is_continue:
    print_board(board)
    player_input(board)
    checkwin
    check_for_tie(board)
    switch_player()
    computer(board)
    checkwin()
    check_for_tie(board)