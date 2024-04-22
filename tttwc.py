import random

def print_board(board):
    # Function to print the Tic-Tac-Toe board
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Function to check if a player has won the game
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def computer_move(board, player):
    # Function for the computer to make a move
    # First, check for a winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                if check_winner(board, player):
                    return
                board[i][j] = " "

    # If no winning move, check for a blocking move (opponent's winning move)
    opponent = "O" if player == "X" else "X"
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = opponent
                if check_winner(board, opponent):
                    board[i][j] = player
                    return
                board[i][j] = " "

    # If no winning or blocking move, make a random move
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = player

def tic_tac_toe():
    # Main function to play Tic-Tac-Toe
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe against the computer!")
    print_board(board)

    while True:
        # Player's move
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] != " ":
            print("That cell is already taken. Try again.")
            continue

        board[row][col] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("You win!")
            break

        if all(all(cell != " " for cell in row) for row in board):
            print("It's a draw!")
            break

        # Computer's move
        print("Computer's move:")
        computer_move(board, "O")
        print_board(board)

        if check_winner(board, "O"):
            print("Computer wins!")
            break

        if all(all(cell != " " for cell in row) for row in board):
            print("It's a draw!")
            break

tic_tac_toe()
