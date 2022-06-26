
# 1board

# 2 display board
# 3 play game
# 4 handle turn
    # check win
    # check rows
    # check coloumns
    # check diagonals
# 5 check tie
# 6 flip player



board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#is game still going?
game_still_going = True

#whos won?or tie?
winner = None

#whos turn?
current_player ="x"


def display_board():
    print(board[0] +"|"+ board[1] + "|" + board[2])
    print(board[3] +"|"+ board[4] + "|" + board[5])
    print(board[6] +"|"+ board[7] + "|" + board[8])

#play a game of tic tac toe
def play_game():
    #display initial board
    display_board()
    # while the game is still going

    while game_still_going:
        #handels a single turn of an arbitrary player
        handle_turn(current_player)
        #check if the game ended
        check_if_game_over()
        #flip to other player
        flip_player()

        #game ended
    if winner =="x" or winner == "o":
        print(winner + " won")
    elif winner == None:
        print("tie.")


# handle a single turn of an arbitrary player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("choose a position from 1-9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Invalid move, You can't go there")

    board[position] = player
    display_board()

def check_if_game_over():
     check_for_winner()
     check_if_tie()

def check_for_winner():
    #set up global variables
    global winner

    row_winner = check_rows()
    coloumn_winner = check_coloumns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif coloumn_winner:
        winner = coloumn_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None


    return

def check_rows():
    # set up global variables
    global game_still_going
    # check if any of the row has same value(and is not empty)
    row_1 = board[0] == board[1] == board[2] !="-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any row does have a match flag that there's a win.
    if row_1 or row_2 or row_3:
        game_still_going = False
        #return the winner (x or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return
def check_coloumns():
    global game_still_going
    # check if any of the coloumn has same value(and is not empty)
    coloumn_1 = board[0] == board[3] == board[6] != "-"
    coloumn_2 = board[1] == board[4] == board[7] != "-"
    coloumn_3 = board[2] == board[5] == board[8] != "-"
    # if any row does have a match flag that there's a win.
    if coloumn_1 or coloumn_2 or coloumn_3:
        game_still_going = False
        # return the winner (x or O)
    if coloumn_1:
        return board[0]
    elif coloumn_2:
        return board[1]
    elif coloumn_3:
        return board[2]

    return
def check_diagonals():
    global game_still_going
    # check if any of the diagonal has same value(and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    # if any diagonal does have a match flag that there's a win.
    if diagonal_1 or diagonal_2:
        game_still_going = False
        # return the winner (x or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]

    return



def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player
    # if the current player was 'x' then change it to 'o'
    if current_player == 'x':
        current_player = 'o'
    elif current_player =='o':
        current_player = 'x'
    return
play_game()



