board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def print_board():
    global board
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("------------")
    for j in range(len(board[0])):
        if j%3==0 and j!=0:
            print("|",end="")
        if j==8:
            print(board[i][j])

        else:
            print(str(board[i][j])+" ",end="")
print("\n*********BEFORE********\n")
print(print_board)

def is_ok(x,y,n):
    global board 
    for i in range(len(board)):
        if board[x][i]==n:
            return False
        if board[y][i]==n:
            return False
    rangex=(x//3) *3
    rangey=(y//3)*3
    for i in range(rangex,rangex+3):
        for j in range(len(board[0])):
            if board[j][i]==n:
                return False
    return True
  

def solve():
    global board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                for k in range(1,10):
                    if is_ok(i,j,k):
                        board[i][j]=k
                        solve()
                        board[i][j]=0
print("\n********AFTER********\n")                       
print(board)
