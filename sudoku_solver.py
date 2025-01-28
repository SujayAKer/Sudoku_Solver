
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return (row, col)
    return None


def is_valid(board, num, position):
    row, col = position


    if num in board[row]:
        return False


    for r in range(len(board)):
        if board[r][col] == num:
            return False


    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == num:
                return False

    return True


def solve(board):

    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty


    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num


            if solve(board):
                return True


            board[row][col] = 0

    return False


sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


print("Original Sudoku Puzzle:")
print_board(sudoku_board)


if solve(sudoku_board):
    print("\nSolved Sudoku Puzzle:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists.")