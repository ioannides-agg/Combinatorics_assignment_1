import numpy as np

# ektypwsh board
def print_board(board):
    for row in board:
        for col in row:
            if col == 1:
                #arxiki thesh
                print("K", end=" ")
            elif col == 2:
                #past move
                print("X", end=" ")
            else:
                #empty cell
                print(".", end=" ")

        print()


# elegxei an mporei na metakinithei o ippoths sthn thesh x,y
def check(x, y, board):
    return x >= 0 and y >= 0 and x < n and y < n and board[x][y] == 0


# h methodos step pernei san orisma thn skakiera
# to current position tou knight, kai thn lista 
# me oles tis prohgoumenes kinhseis
def step(board, pos, past_moves):
    # kaloume thn global s (pou exei oristei pio katw) wste na 
    # mporoume na ayksisoume thn metavlhth s pou einai se poio vhma eimaste
    global s
    s += 1

    # an to mhkos twn past_moves einai megalytero iso tou n^2, 
    # pou shmainei oti o knight exei kanei n^2 kinhseis
    # (oles tis kinhseis tou board)
    if len(past_moves) >= n**2:
        # printaroume tis kinhseis pou ekane 
        # kai posa vhmata xreiasthkan gia na vroume thn lysh
        print("-----------------------------------")
        print(past_moves)
        print("-----------------------------------")
        print("Solution found at Step:{}".format(s))
        return True
    
    # proypologizoumai to offset twn kinhsewn tou knight ston rows/columns aksona
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    move = list(zip(move_x, move_y))
    
    #kai gia kathe kinhsh
    for i in range(8):
        #ypologizoumai to neo position
        new_x = pos[0] + move[i][0]
        new_y = pos[1] + move[i][1]
        #an einai asfales to position tote
        if check(new_x, new_y, board):
            #markaroume to kouti oti o knight exei 
            # perasei apo ekei kai prosthetoume sthn lista 
            # thn nea kinhsh
            board[new_x][new_y] = 2
            past_moves.append((new_x, new_y))

            # kaloume to recursive function step etsi wste na 
            # kleithei mexri na ikanopoieitai h len(past_moves) >= n**2:
            # opou sthn sygkekrimenh periptwsh kanoum return true apo thn teleytaia step 
            # mexri thn prwth
            if step(board, (new_x, new_y), past_moves):
                return True
            
            # an to step den ikanopoiethei anairoumai thn kinhsh
            board[new_x][new_y] = 0
            past_moves.remove((new_x, new_y))
    
    # an kamia kinhsh sthn moves den ikanopoiei tis proypotheseis 
    # mas epistrefoume False sthn prohgoumenh step wste na ginei recalculated h kinhsh
    return False
        



def main():
    # arxikopoioumai thn global variable s, n
    global s
    s = 0
    global n
    n = 8
    # xrhsimopoioumai numpy gia thn dhmiourgeia tou n*n board
    board = np.zeros((n,n), dtype=int)
    # zhtame apo ton xrhsth thn prwth kinhsh
    i = 0
    j = 0

    # orizoume thn prwth kinhsh
    board[i][j] = 1
    pos = (i,j)
    
    # kai thn prosthetoume sthn lista twn past_moves
    past_moves = []
    past_moves.append(pos)

    # kaloume thn step.
    step(board,pos, past_moves)

if __name__ == "__main__":
    main()