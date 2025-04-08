def is_safe(board, current_row, current_col, size):
    # Check vertically upward
    for row in range(current_row):
        if board[row][current_col] == 1:
            return False

    # Check upper left diagonal
    row, col = current_row, current_col
    while row >= 0 and col >= 0:
        if board[row][col] == 1:
            return False
        row -= 1
        col -= 1

    # Check upper right diagonal
    row, col = current_row, current_col
    while row >= 0 and col < size:
        if board[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True


def solve_n_queens(board, row, size):
    # Base case: all queens placed
    if row >= size:
        return True

    # Try placing a queen in each column of the current row
    for col in range(size):
        if is_safe(board, row, col, size):
            board[row][col] = 1  # Place queen

            if solve_n_queens(board, row + 1, size):  # Recurse to next row
                return True

            board[row][col] = 0  # Backtrack

    return False  # No valid placement found


def display_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))


def main():
    size = int(input("Enter number of Queens: "))
    board = [[0 for _ in range(size)] for _ in range(size)]

    if solve_n_queens(board, 0, size):
        print("\nSolution:")
        display_board(board)
    else:
        print("No solution exists.")


if __name__ == "__main__":
    main()
