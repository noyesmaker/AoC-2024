#region Part 1
def horizontal_f(matrix, i, j):
    retval = 0

    if (len(matrix[i]) - j >= 4) and (matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i][j+3] == "XMAS"):
        retval = 1
    return retval

def horizontal_b(matrix, i, j):
    retval = 0
    # distance = len(matrix[i]) - j

    # print("Distance:", distance)
    # print(matrix[i][j] + matrix[i][j-1] + matrix[i][j-2] + matrix[i][j-3])
    if (j >= 3) and (matrix[i][j] + matrix[i][j-1] + matrix[i][j-2] + matrix[i][j-3] == "XMAS"):
        retval = 1
    return retval

def vertical_f(matrix, i, j):
    retval = 0
    if (len(matrix) - i >= 4) and (matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j] == "XMAS"):
        retval = 1
    return retval

def vertical_b(matrix, i, j):
    retval = 0
    if (i >= 3) and (matrix[i][j] + matrix[i-1][j] + matrix[i-2][j] + matrix[i-3][j] == "XMAS"):
        retval = 1
    return retval

def diagonal_br(matrix, i, j): 
    retval = 0
    if (len(matrix[i]) - j >= 4) and (len(matrix) - i >= 4) and (matrix[i][j] + matrix[i+1][j+1] + matrix[i+2][j+2] + matrix[i+3][j+3] == "XMAS"):
        retval = 1
    return retval

def diagonal_tl(matrix, i, j): 
    retval = 0
    if (i >= 3) and (j >= 3) and (matrix[i][j] + matrix[i-1][j-1] + matrix[i-2][j-2] + matrix[i-3][j-3] == "XMAS"):
        retval = 1
    return retval

def diagonal_tr(matrix, i, j): 
    retval = 0
    if (i >= 3) and (len(matrix[i]) - j >= 4) and (matrix[i][j] + matrix[i-1][j+1] + matrix[i-2][j+2] + matrix[i-3][j+3] == "XMAS"):
        retval = 1
    return retval

def diagonal_bl(matrix, i, j): 
    retval = 0
    if (len(matrix) - i >= 4) and (j >= 3) and (matrix[i][j] + matrix[i+1][j-1] + matrix[i+2][j-2] + matrix[i+3][j-3] == "XMAS"):
        retval = 1
    return retval
#endregion

#region Part 2
def xmas(matrix, i, j):
    retval = 0

    if (i >= 1) and (j >= 1) and (len(matrix) - i >= 2) and (len(matrix[i]) - j >= 2) and (matrix[i][j] == 'A'):
        
        tl = matrix[i-1][j-1]
        br = matrix[i+1][j+1]
        tr = matrix[i-1][j+1]
        bl = matrix[i+1][j-1]

        print(tl,'.',tr)
        print('.','A','.')
        print(bl, '.', br)

        if ((tl == 'M' and br == 'S') or (tl == 'S' and br == 'M')) and \
           ((tr == 'M' and bl == 'S') or (tr == 'S' and bl == 'M')):
            print("match!")
            retval = 1

    return retval
#endregion
with open("input.txt") as input:
    grid = []

    for line in input:
        entry = line.split()
        grid.append(list(str(line.split()[0])))
    
    sumxmas = 0
    sumcrossmas = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            sumxmas += horizontal_f(grid, i, j) + horizontal_b(grid, i, j) + \
                   vertical_f(grid, i, j) + vertical_b(grid, i, j) + \
                    diagonal_tl(grid, i, j) + diagonal_tr(grid, i,j) + \
                    diagonal_bl(grid, i, j) + diagonal_br(grid, i,j)
            
            sumcrossmas += xmas(grid, i, j)
    
    print("Sum XMAS:", sumxmas)
    print("Sum CROSSMAS:", sumcrossmas)
