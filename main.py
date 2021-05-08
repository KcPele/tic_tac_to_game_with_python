# --------Global Variable ----------

# Game board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# if fgame is still going
game_still_going = True

# Who won? or tie
winner = None

#Who turns player
current_player = "X"

# Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#play tic tac toe game
def play_game():
    
    # Display initial board
    display_board()

    # while game is still going
    while game_still_going:

        handle_turn(current_player)
        
        #check if the game has ended
        check_if_game_over()

        #Flip to the other player
        flip_player()
        
        # The game has ended
    if winner == "X" or winner == "0":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")
    



def handle_turn(player):

    print(player + "'s turn")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1
    
        if board[position] == "-":
            valid = True
        else:
            print("You cant go there. Go again")

    board[position] = player
    display_board()


def check_if_game_over():
    check_if_winner()
    check_if_tie()

def check_if_winner():

    global winner
    #check row
    
    row_winner = check_rows()
    #check column
    columns_winner = check_columns()
    #check diagonal
    diagonal_winner = check_diagonal()

    if row_winner:
       winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
 
    return

def check_rows():
    # Set up global variable
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    
    #IF any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    #return the winner X or 0
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    
    #IF any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    #return the winner X or 0
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonal():
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    
    #IF any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    #return the winner X or 0
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return
    
def check_if_tie():
    #global
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    #global variable
    global current_player

    if current_player == "X":
        current_player = "0"
    elif current_player == "0":
        current_player = "X"
    return

play_game()



#board
#display board
#play game
#handle turn
#check win
 #check rows
 #check column
 #check diagonals
#check tie
#flip player