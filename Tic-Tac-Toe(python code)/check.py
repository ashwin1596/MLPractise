
#---check for same row
def check_row(matrix):

    for i in range(3):
        if matrix[i][0] == matrix[i][1]:
            if matrix[i][1] == matrix[i][2]:
                if matrix[i][0] =="X":
                    return 1
                elif matrix[i][0] =="O":
                    return 2

#---check for same column
def check_column(matrix):

    for j in range(3):
        if matrix[0][j] == matrix[1][j]:
            if matrix[1][j] == matrix[2][j]:
                if matrix[0][j] == "X":
                    return 1
                elif matrix[0][j] =="O":
                    return 2


def check_diagonal(matrix):
    #-------leading diagonal
    if matrix[0][0]==matrix[1][1]:
        if matrix[1][1]==matrix[2][2]:
            if matrix[0][0]=="X":
                return 1
            elif matrix[0][0]=="O":
                return 2
    #--------second diagonal
    if matrix[0][-1]==matrix[1][-2]:
        if matrix[1][-2]==matrix[2][-3]:
            if matrix[0][-1]=="X":
                return 1
            elif matrix[0][-1]=="O":
                return 2



def check(matrix):

    winner=check_row(matrix)

    if winner==None:
        winner=check_column(matrix)

    if winner==None:
        winner=check_diagonal(matrix)

    return winner








