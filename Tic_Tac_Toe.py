
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True

winner = None

current_player = "x"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + "\t1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "\t4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "\t7 | 8 | 9")


def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "x" or winner == "0":
        print(winner + " won.")
    elif winner == None:
        print("tie!")


def check_if_game_over():
    check_if_win()
    check_if_tie()


def flip_player():
    global current_player

    if current_player == "x":
        current_player = "0"
    elif current_player == "0":
        current_player = "x"

    return


def check_if_win():
    global winner
    # check row
    row_winner = check_row()
    # check column
    column_winner = check_column()
    # check diagonal
    diagonal_winner = check_diagonal()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_row():
    global game_still_going

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def check_column():
    global game_still_going

    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        game_still_going = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return


def check_diagonal():
    global game_still_going

    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[6] == board[4] == board[2] != "-"

    if diag1 or diag2:
        game_still_going = False
    if diag1:
        return board[0]
    elif diag2:
        return board[6]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def handle_turn(player):
    print(player + "'s turn")
    pos = input("choose position from 1-9 or press q to quit: ")
    if pos == "q":
        exit()
    valid = False
    while not valid:
        while pos not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            pos = input("Invalid choice!. Enter the no again: ")

        pos = int(pos) - 1

        if board[pos] == "-":
            valid = True
        else:
            print("You cannot go there!")

    board[pos] = player

    display_board()


play_game()
