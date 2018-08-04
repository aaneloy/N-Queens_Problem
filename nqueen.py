import copy
def input_size():
    while True:

        try:
            size = int(input('Enter NXN Board Size \n'))
            if 0 < size < 4:
                print("Enter attlist size of 4")
                continue
            return size
        except ValueError:
            print("Invalid value entered. Enter again")


def board_size(size):
    board = [0] * size
    for i in range(size):
        board[i] = [0] * size
    return board


def print_solution(solutions, size):
    for sol in solutions:
        for row in sol:
            print(row)
        print()


def is_safe(board, row, col, size):

    # check row on left side
    for iy in range(col):
        if board[row][iy] == 1:
            return False

    ix, iy = row, col
    while ix >= 0 and iy >= 0:
        if board[ix][iy] == 1:
            return False
        ix -= 1
        iy -= 1

    jx, jy = row, col
    while jx < size and jy >= 0:
        if board[jx][jy] == 1:
            return False
        jx += 1
        jy -= 1

    return True


def solve(board, col, size):
    # base case
    if col >= size:
        return

    for i in range(size):
        if is_safe(board, i, col, size):
            board[i][col] = 1
            if col == size - 1:
                add_solution(board)
                board[i][col] = 0
                return
            solve(board, col + 1, size)
            board[i][col] = 0


def add_solution(board):
    """Saves the board state to the global variable 'solutions'"""
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)


size = input_size()
board = board_size(size)
solutions = []
solve(board, 0, size)
print_solution(solutions, size)

