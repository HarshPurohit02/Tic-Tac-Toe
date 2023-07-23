#Function to print Tic Tac Toe Board.
def print_tic_t_t(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}  ".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}  ".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}  ".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


#Function to print the scoreboard for the game.
def print_scoreboard(score_board):
    print("\t----------------------------------")
    print("\t    SCOREBOARD FOR TIC TAC TOE    ")
    print("\t----------------------------------")

    players = list(score_board.keys())
    print("\t   ", players[0], "\t   ",score_board[players[0]])
    print("\t   ", players[1], "\t   ",score_board[players[1]])

    print("\t----------------------------------")


#Function to check if the player has won the game.
def check_winner(player_position, current_player):

    #All possible winning combinations for the players.
    soln = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 4, 7],[2, 5, 8],[3, 6, 9],[1, 5, 9],[3, 5, 7]]

    #Loop to check if any winning combination satisfies or not.
    for x in soln:
        if all(y in player_position[current_player] for y in x):

            #Return True if any winning combination satisfies in the iteration.
            return True
    #Return False if above condition is not satisfied.
    return False


#Function to check if the function is draw.
def check_draw(player_position):
    if len(player_position['X']) + len(player_position['O']) == 9:
        return True
    return False


#Function for a single tic tac toe game.
def single_game(current_player):

    #Represents the tic tac  toe.
    values = [' ' for x in range(9)]

    #Stores the position occupied by X and 0
    player_position = {'X':[], 'O':[]}

    #game loop for a single game of tic tac toe
    while True:
        print_tic_t_t(values)

        #try exception block for Move input.
        try:
            print("Player ", current_player, "turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue

        #Sanity check for MOVE Input.
        if move < 1 or move > 9:
            print("Please choose right number between 1 ro 9")
            continue

        #Check if the cell is occupied or not.
        if values[move-1] != ' ':
            print('Box already Occupied!!')
            continue

        #Update game status.

        #Updating board status.
        values[move-1] = current_player

        #Updating player positions
        player_position[current_player].append(move)

        #Function call for checking winner.
        if check_winner(player_position, current_player):
            print_tic_t_t(values)
            print("Player", current_player, "Has won the Game!!!")
            print("\n")
            return current_player
        
        #Function call for checking draw game.
        if check_draw(player_position):
            print_tic_t_t(values)
            print("Game is Draw!!")
            print("\n")
            return 'D'
        
        #Switch player moves
        if current_player == 'X' :
            current_player = 'O'
        else:
            current_player = 'X'

if __name__ == "__main__":

    print("Player 1 Details")
    play1 = input("Enter the name of the player : ")
    print("\n")

    print("Player 2 Details")
    play2 = input("Enter the name of the player : ")
    print("\n")


#Stores the player who choses X and O
current_player = play1

#Stores the choice of players chracters.
player_choice = {'X' : "", 'O' : ""}

#stores the options
options = ['X', 'O']

#Stores the scoreboard details
score_board = {play1: 0, play2: 0}
print_scoreboard(score_board)


#Game loop for series of tic tac toe.
#The loop runs till either of the payers choose to quit.
while True:

    #player choice menu
    print("Turn to choose for", current_player)
    print("Enter 1 for X")
    print("Enter 2 for O")
    print("Enter 3 for quit")

    #Try exception for choice input.
    try:
        choice = int(input())
    except ValueError:
        print("Wrong Input!!! Try Again\n")
        continue

    #conditions for playerchoice
    if choice == 1:
        player_choice['X'] = current_player
        if current_player == play1:
            player_choice['O'] = play2
        else:
            player_choice['O'] = play1

    elif choice == 2:
        player_choice['O'] = current_player
        if current_player == play1:
            player_choice['X'] = play2
        else:
            player_choice['X'] = play1

    elif choice == 3:
        print("Final scores")
        print_scoreboard(score_board)
        break

    else:
        print("Wrong choice!! Try again\n")

    #Stores winner in single game of tic tac toe
    winner = single_game(options[choice-1])

    #scoreboard edits according to winner
    if winner != 'D':
        player_won = player_choice[winner]
        score_board[player_won] = score_board[player_won] + 1

    print_scoreboard(score_board)
    #Switch players who choosesX or O
    if current_player == play1:
        current_player = play2
    else:
        current_player = play1