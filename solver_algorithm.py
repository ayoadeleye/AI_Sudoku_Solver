board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(input_board):
    find = empty_cell(input_board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(input_board, i, (row, col)):
            input_board[row][col] = i

            if solve(input_board):
                return True

            input_board[row][col] = 0

    return False


def valid(input_board, num, pos):
    # Check row
    for i in range(len(input_board[0])):
        if input_board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(input_board)):
        if input_board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check input_boardx
    input_boardx_x = pos[1] // 3
    input_boardx_y = pos[0] // 3

    for i in range(input_boardx_y*3, input_boardx_y*3 + 3):
        for j in range(input_boardx_x * 3, input_boardx_x*3 + 3):
            if input_board[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(input_board):
    for i in range(len(input_board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(input_board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(input_board[i][j])
            else:
                print(str(input_board[i][j]) + " ", end="")


def empty_cell(input_board):
    for row_idx, row in enumerate(input_board):
        for col_idx, col in enumerate(row):
            if row == 0 and col == 0:
                return row_idx, col_idx
