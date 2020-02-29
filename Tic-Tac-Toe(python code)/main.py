import ui

cont='y'
p1=0
p2=0

print("""\n\n\n------------------------------------------------------------Welcome to Tic Tac Toe-----------------------------------------------------------------""")
print("""Note: Give input as 'row,column'- a number, then a comma, then a number""")
while cont=='y':
    matrix = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]
    winner=ui.user_interface(matrix)

    if winner==1:
        print ("Congratulations!!! Player1 has won")

    elif winner==2:
        print("Congratulations!!! Player2 has won")

    else:
        print("Game over!!!")

    cont=input("Want to play more and tally which one of you has won more(y/n)")


    if winner==1:
        p1+=1
    elif winner==2:
        p2+=1


    print ("Player1 has won",p1," games")
    print ("Player2 has won",p2," games")