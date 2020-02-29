import check

def user_interface(matrix):
    nmp=0
    curr_player=1

    user_input=input("\nWhat is your first move\n")

    user_input.strip()
    next_move=user_input.split(",")
    i=int(next_move[0])
    j=int(next_move[1])
    matrix[i-1][j-1]="X"



    print(""" ___________""")
    for i in range(3):

        for j in range(3):
            if j == 0:
                print("|", matrix[i][j], "|", end='')

            else:
                print("", matrix[i][j], "|", end='')

        print("")
        print("""|___|___|___| """)

    winner=check.check(matrix)
    if winner!=None:
        return winner
    nmp+=1
    curr_player=2

    while nmp<9:                                   #--------nmp is next_move_possible
        try:
            user_input = input("What is your next move\n")

            user_input.strip()
            next_move = user_input.split(",")
            i = int(next_move[0])
            j = int(next_move[1])

            if matrix[i-1][j-1] != " ":
                print("Place is already occupied,give another move")
                user_input = input("What is your next move\n")
                user_input.strip()
                next_move = user_input.split(",")
                i = int(next_move[0])
                j = int(next_move[1])

            if curr_player==1:
                matrix[i - 1][j - 1] = "X"
                curr_player = 2

            else:
                matrix[i - 1][j - 1] = "O"
                curr_player=1

            print(""" ___________""")
            for i in range(3):

                for j in range(3):
                    if j==0:
                        print("|",matrix[i][j],"|",end='')

                    else:
                        print("",matrix[i][j], "|",end='')

                print("")
                print("""|___|___|___| """)

            winner = check.check(matrix)
            if winner != None:
                return winner

            nmp+=1


        except:
            print ("invalid move!!!!")

