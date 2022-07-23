
# validates if i is already in the current row, column or 3x3 grid
def valid(row, col, board, i):
    # checks the 3x3 grid
    def cubes():
        if row<=2 and col<=2:
            return (i not in board[0:3, 0:3])
        
        elif row<=2 and 3<=col<=5:
            return (i not in board[0:3, 3:6])
        
        elif row<=2 and 6<=col<=8:
            return (i not in board[0:3, 6:9])
        
        elif 3<=row<=5 and col<=2:
            return (i not in board[3:6, 0:3])
        
        elif 3<=row<=5 and 3<=col<=5:
            return (i not in board[3:6, 3:6])
        
        elif 3<=row<=5 and 6<=col<=8:
            return (i not in board[3:6, 6:9])
        
        elif 6<=row<=8 and col<=2:
            return (i not in board[6:9, 0:3])
        
        elif 6<=row<=8 and 3<=col<=5:
            return (i not in board[6:9, 3:6])
        
        elif 6<=row<=8 and 6<=col<=8:
            return (i not in board[6:9, 6:9])
        
    return (i not in board[row, ::] and i not in [r[col] for r in board] and cubes())      
        
# check if current position is an available spot
def spot_is_zero(row, col, board):
    return (board[row][col] == 0)

# check if board has been solved
def check_full(board):
    check = 0
    for row in board:
        if 0 in row:
            check+=1 
    return (check==0)


def solve(row, col, board):
    
    if check_full(board):
        return True
    
    # boundary case
    if col+1 > len(board[row]):
        row = row + 1
        col = 0
   
    # if open space
    if spot_is_zero(row, col, board):
        # check every number
        for i in range(1,10):
            if valid(row, col, board, i):
                board[row][col] = i
                if solve(row, col+1, board):
                    return True
        
        # contingency check 
        if check_full(board):
            return True
        
        # else backtrack
        board[row][col] = 0
      
    else:
        solve(row, col+1, board)


def sudoku(board):
    if solve(0, 0, board):
        print(board)
    else:
        print('No possible solution')
