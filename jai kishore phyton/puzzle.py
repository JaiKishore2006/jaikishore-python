import random

# Function to print the board
def print_board(board):
    for row in board:
        print(row)

# Function to find coordinates of empty space
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return None

# Function to check if the board is solved
def is_solved(board):
    n = len(board) * len(board[0])
    return all(board[i][j] == i * len(board[0]) + j + 1 for i in range(len(board)) for j in range(len(board[0]) - 1)) and board[len(board) - 1][len(board[0]) - 1] == 0

# Function to shuffle the board
def shuffle_board(board, moves=100):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for _ in range(moves):
        i, j = find_empty(board)
        move = random.choice(directions)
        ni, nj = i + move[0], j + move[1]
        if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
            board[i][j], board[ni][nj] = board[ni][nj], board[i][j]

# Function to check if a move is valid
def is_valid_move(board, direction):
    i, j = find_empty(board)
    ni, nj = i + direction[0], j + direction[1]
    return 0 <= ni < len(board) and 0 <= nj < len(board[0])

# Function to make a move
def make_move(board, direction):
    i, j = find_empty(board)
    ni, nj = i + direction[0], j + direction[1]
    board[i][j], board[ni][nj] = board[ni][nj], board[i][j]

# Main game loop
def play_game():
    board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]]  # Initial board configuration
    shuffle_board(board)  # Shuffle the board

    while not is_solved(board):
        print_board(board)
        direction = input("Enter direction (up/down/left/right): ").strip().lower()

        if direction == 'up' and is_valid_move(board, (-1, 0)):
            make_move(board, (-1, 0))
        elif direction == 'down' and is_valid_move(board, (1, 0)):
            make_move(board, (1, 0))
        elif direction == 'left' and is_valid_move(board, (0, -1)):
            make_move(board, (0, -1))
        elif direction == 'right' and is_valid_move(board, (0, 1)):
            make_move(board, (0, 1))
        else:
            print("Invalid move. Please enter again.")

    print("Congratulations! You solved the puzzle.")
