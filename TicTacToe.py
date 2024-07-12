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


def win_check(board, solutions, player1, player2):
    for tuple in solutions:
        player1Spaces = 0
        player2Spaces = 0

        for num in tuple:
            if board[str(num)] == player1:
                player1Spaces += 1
            elif board[str(num)] == player2:
                player2Spaces += 1

        if player1Spaces == 3:
            winner = 1
        elif player2Spaces == 3:
            winner = 2
        else:
            winner = 0
    print("checking")
    return winner


j = 1

print("Spaces on the board are represented by numbers, so to place your X or O in a space, type the space number you want to use.")
tictactoe_board(ticTacToe)
for index, item in enumerate(ticTacToe, 1):
    ticTacToe[str(index)] = " "

for i in range(1,10):
    if j == 1:
        while j == 1:
            print("Player 1, select a number from the board (only 1-9)")
            space = input()

            #try:
            if i >= 5 and win_check(ticTacToe, possibleSolutions, "X", "O") == 1 or i >= 5 and win_check(ticTacToe, possibleSolutions, "X", "O") == 2:
                    j = 2
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
                        j = 2
            #except:
                #print("You did not type a valid number or input. Please try again!")
                #tictactoe_board(ticTacToe)
                #pass
            
    elif j == 2:
        while j == 2:
            print("Player 2, select a number from the board (only 1-9)")
            space = input()

            #try:
            if i >= 5 and win_check(ticTacToe, possibleSolutions, "X", "O") == 1 or i >= 5 and win_check(ticTacToe, possibleSolutions, "X", "O") == 2:
                    j = 1
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
                        j = 1
            #except:
                #print("You did not type a valid number or input. Please try again!")
                #tictactoe_board(ticTacToe)
                #pass

if win_check(ticTacToe, possibleSolutions, "X", "O") == 1:
    print("Player 1 has won the game!")
elif win_check(ticTacToe, possibleSolutions, "X", "O") == 2:
    print("Player 2 has won the game!")
else:
    print("This game has concluded in a tie!")