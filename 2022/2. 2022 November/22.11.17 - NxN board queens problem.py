"""
You have an N by N board. 

Write a function that, given N, returns the number of possible arrangements 
of the board where N queens can be placed on the board without threatening each other,
i.e. no two queens share the same row, column, or diagonal.
"""

def N_queens_problem(N):

    board = list()

    #Board generation
    for n in range(N):
        line = [False] * N
        board.append(line)
        
    
    #Checks if queen lies on horizontal of coords
    def check_horizontal(y_val):
        return (sum(board[y_val]) >= 1)
    
    #Check if queen lies on vertical of coords
    def check_vertical(x_val):
        column = list()
        for row in range(len(board)):
            column.append(board[row][x_val])
        return (sum(column)>=1)

    #Checks if lower left diagonal is occupied by queen
    def lower_left_check(y_val, x_val):
        line = list()
        for i, j in zip(range(y_val, N, 1), range(x_val, -1, -1)):
            line.append(board[i][j])
        return (sum(line) >= 1)
    
    #Checks if upper left diagonal is occupied by queen
    def upper_left_check(y_val, x_val):
        line = list()
        for i, j in zip(range(y_val, -1, -1), range(x_val, -1, -1)):
            line.append(board[i][j])
        return (sum(line) >= 1)
    
    #Checks if lower right diagonal is occupied by queen
    def lower_right_check(y_val, x_val):
        line = list()
        for i, j in zip(range(y_val, N, 1), range(x_val, N, 1)):
            line.append(board[i][j])
        return (sum(line) >= 1)
    
    #Checks if upper right diagonal is occupied by queen
    def upper_right_check(y_val, x_val):
        line = list()
        for i, j in zip(range(y_val, -1, -1), range(x_val, N, 1)):
            line.append(board[i][j])
        return (sum(line) >= 1)

    #Runs all checks
    def run_checks(y_val, x_val):
        return (check_horizontal(y_val)
        or check_vertical(x_val)
        or lower_left_check(y_val,x_val)
        or upper_left_check(y_val, x_val)
        or lower_right_check(y_val,x_val)
        or upper_right_check(y_val,x_val))
  
    #Create empty list to store solved board
    solved_boards = list()



    def check_if_solution_is_unique(solution):
        if solution not in solved_boards:
            solved_boards.append(solution)
            print("NEW SOLUTION")
    

    #Starting position
    for i in range(N):
        for j in range(N):

            board = list()
            for n in range(N):
                line = [False] * N
                board.append(line)

            board[i][j] = True

            number_of_queens_to_place = N-1
            print(number_of_queens_to_place)


            for y in range(N):
                for x in range(N):

                    queen_owned = run_checks(y,x)
                    if queen_owned == False:
                        board[y][x] = True
                        number_of_queens_to_place -= 1

                    
                if number_of_queens_to_place == 0:
                    check_if_solution_is_unique(board)

            for line in board:
                print(line)

            print("----------------------------------------------")
    
    return(len(solved_boards))
                    


                    



print(N_queens_problem(6))