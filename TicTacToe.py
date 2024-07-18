ticTacToe = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}
possibleSolutions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def tictactoe_board(dashes):
    print("==========================")
    for index, string in enumerate(dashes, 1):
        if index % 3 == 0 and index != 9:
            print("", dashes[str(index)], "")
            print("---+---+---")

        elif index % 3 != 0 and index != 9:
            print("", dashes[str(index)], "", end= '|')

        else:
            print("", dashes[str(index)], "")

def player1Won(board, solutions):
    win = None
    for tuple in solutions:
        if board[str(tuple[0])] == "X" and board[str(tuple[1])] == "X" and board[str(tuple[2])] == "X":
            win = True
            break
        else:
            pass

    if win != True:
        win = False
    return win
        
def player2Won(board, solutions):
    win = None
    for tuple in solutions:
        if board[str(tuple[0])] == "O" and board[str(tuple[1])] == "O" and board[str(tuple[2])] == "O":
            win = True
            break
        else:
            pass
        
    if win != True:
        win = False
    return win


player = 1

print("Spaces on the board are represented by numbers, so to place your X or O in a space, type the space number you want to use.")
tictactoe_board(ticTacToe)
for index, item in enumerate(ticTacToe, 1):
    ticTacToe[str(index)] = " "

for turns in range(1,10):
    if player == 1:
        while player == 1:
            if turns >= 5 and player1Won(ticTacToe, possibleSolutions) or turns >= 5 and player2Won(ticTacToe, possibleSolutions):
                break
            else:
                print("Player 1, select a number from the board (only 1-9)")
                space = input()

            try:

                if ticTacToe[space] == "O":
                    print("That space is already taken! Try again!")
                    tictactoe_board(ticTacToe)
                    pass
                else:
                    
                    if ticTacToe[space] == "X":
                        print("You have already used this space! Try again!")
                        tictactoe_board(ticTacToe)
                        pass
                    else:
                        ticTacToe[space] = "X"
                        tictactoe_board(ticTacToe)
                        player = 2
            except:
                print("You did not type a valid number or input. Please try again!")
                tictactoe_board(ticTacToe)
                pass
            
    elif player == 2:
        while player == 2:
            if turns >= 5 and player1Won(ticTacToe, possibleSolutions) or turns >= 5 and player2Won(ticTacToe, possibleSolutions):
                break
            else:
                print("Player 2, select a number from the board (only 1-9)")
                space = input()

            try:

                if ticTacToe[space] == "X":
                    print("That space is already taken! Try again!")
                    tictactoe_board(ticTacToe)
                    pass
                else:
                    
                    if ticTacToe[space] == "O":
                        print("You have already used this space! Try again!")
                        tictactoe_board(ticTacToe)
                        pass
                    else:
                        ticTacToe[space] = "O"
                        tictactoe_board(ticTacToe)
                        player = 1
            except:
                print("You did not type a valid number or input. Please try again!")
                tictactoe_board(ticTacToe)
                pass

if player1Won(ticTacToe, possibleSolutions):
    print("Player 1 has won the game!")

elif player2Won(ticTacToe, possibleSolutions):
    print("Player 2 has won the game!")

else:
    print("This game has concluded in a tie!")