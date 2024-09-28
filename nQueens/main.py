import numpy as np

# megethos skakieras 
global N
N = 8
 
# ektuposi board
def printBoard(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q",end=" ")
            else:
                print(".",end=" ")
        print()

# elegxei an mporei na mpei queen sto board[row][col]
# col = posa queens exoun topothetithei
# row = row pou vriskomaste
# i = col pou tsekaroume
def check(board, row, col):
 
    # elegxei an uparxei queen sthn seira row
    for i in range(col):
        if board[row][i] == 1:
            return False
 
    # elegxei an uparxei queen sthn panw diagwnio
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    # elegxei an uparxei queen sthn katw diagwnio
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    return True
 

# h synartisi step pernei ws parametrous
# thn skakiera kai th sthlh sthn opoia 
# vriskete o algorithmos
def step(board, col):

    # elegxei an exoume prospelasei oles tis sthles kai
    # termatizei to step
    if col >= N:
        return True
    

    # for loop h opoia sthn opoia elegxete se poia grammi
    # tha topothetitei to queen
    for i in range(N):
        if check(board, i, col):

            # vazoume vasilisa
            board[i][col] = 1

            # pame sthn epomenh sthlh, kai an to apotelesma ths epomenhs
            # topothethshs einai true tote ginete confirm kai h topothethsh sto twrino column.
            # ara sthn prgmatikothta to 1 ginete confirm apo to telos
            # pros thn arxh, wste na eksetasoume oles tis periptwseis.
            sucessful_step = step(board, col + 1)
            if sucessful_step:
                return True
            
            # alliws kanoume backtrack kai afairoume to queen pou prosthesame
            # kanei return false giati to x+1 queen
            # den exei pou na topothetitei ara to queen x prepei na allaksei thesh
            else:
                board[i][col] = 0
            
    return False
 
def nQueens():

    # gemizei thn skakiera me mhdenika (megethos n x n)
    board = np.zeros((N,N))


    # elegxei oti o algorithmos einai efiktos kai
    # kanei print to apotelesma
    if step(board, 0) == True:
        printBoard(board)
        return True
    else:
        print("Solution does not exist")
        return False
 
 
if __name__ == '__main__':
    nQueens()
 