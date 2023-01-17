"""
The word can be constructed from letters of sequentially adjacent cell, where "adjacent"
 cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
"""

grid = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

def snake_word_search(grid, word):

    word = [x.upper() for x in word]
    print(word)

    #1. for each element in grid, start search
        #a. if 
    
    def snake_search(y_val, x_val, index):

        point = grid[y_val, x_val]
        if point == word[index]:
            index+=1

        if index == (len(word)-1):
            return True
        
        def get_all_neighbours()


        


    for y_val in range(len(grid)):
        for x_val in range(len(grid[0]):
            origin = grid[y_val][x_val]
            if origin = word[0]:
                snake_search(y_val,x_val, 0)
            


snake_word_search(grid,"snake")