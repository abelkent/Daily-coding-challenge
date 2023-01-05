"""
Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""


islands = ["1 0 0 0 0",
            "0 0 1 1 0",
            "0 1 1 0 0",
            "0 0 0 0 0",
            "1 1 0 0 1",
            "1 1 0 0 1"]


def island_counter(matrix):
    
    matrix = [line.split(" ") for line in matrix]
    

    island_count = int(0)
    island_coords = list()
    
    def island_check(y_coord, x_coord):

        island_coords.append([y_coord, x_coord])

        neighbours = list()

        #Above
        if y_coord != 0:
            neighbours.append([y_coord-1,x_coord])

        #Below
        if y_coord != len(matrix):
            neighbours.append([y_coord+1,x_coord])

        #Left
        if x_coord != 0:
            neighbours.append([y_coord,x_coord-1])
        
        #Right
        if x_coord != len(matrix[0]):
            neighbours.append([y_coord, x_coord+1])

        for index in range(len(neighbours)):
            ##FINISH THIS
        
            

    for y_point in range(len(matrix)):
        for x_point in range(len(matrix[0])):
            if ([y_point, x_point] not in island_coords) and (matrix[y_point][x_point] != "0"):
                island_count += 1
                island_check(y_point, x_point)            
            




island_counter(islands)