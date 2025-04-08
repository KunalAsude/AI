# Function to print the board in 3x3 format
def print_board(board):
    for i in range(9):
        if i % 3 == 0:
            print()  # Move to new line after every 3 elements
        print("_" if board[i] == -1 else board[i], end=" ")
    print()

def heuristic(current, goal):
    h = 0
    for i in range(9):
        if current[i] != -1:  # Skip the empty tile
            goal_pos = goal.index(current[i]) 
            h += abs(goal_pos // 3 - i // 3) + abs(goal_pos % 3 - i % 3) 
    return h

# Move the empty tile (-1) in the given direction if possible
def move_tile(board, direction):
    idx = board.index(-1)
    new_board = board[:]  

    if direction == "left" and idx % 3 != 0:
        new_board[idx], new_board[idx - 1] = new_board[idx - 1], new_board[idx]
    elif direction == "right" and idx % 3 != 2:
        new_board[idx], new_board[idx + 1] = new_board[idx + 1], new_board[idx]
    elif direction == "up" and idx >= 3:
        new_board[idx], new_board[idx - 3] = new_board[idx - 3], new_board[idx]
    elif direction == "down" and idx < 6:
        new_board[idx], new_board[idx + 3] = new_board[idx + 3], new_board[idx]
    return new_board

# Try all 4 possible moves and return the one with the lowest heuristic
def best_move(board, goal):
    directions = ["left", "right", "up", "down"]
    best = None
    lowest = float('inf')  
    for direction in directions:
        new_board = move_tile(board, direction)
        if new_board != board: 
            h = heuristic(new_board, goal)
            if h < lowest:
                lowest = h
                best = new_board
    return best

# Main solving function
def solve_puzzle(start, goal):
    current = start[:]  
    moves = 0           

    # Loop until we reach the goal state
    while current != goal:
        print(f"\nMove {moves}:")
        print_board(current)
        current = best_move(current, goal) 
        moves += 1

    print(f"\nSolved in {moves} moves!")
    print_board(current)

def main():
    start = []
    goal = []

    print("Enter Start State (-1 for empty) (all 9 numbers separated by space):")
    start = list(map(int, input().split()))

    print("Enter Goal State (all 9 numbers separated by space):")
    goal = list(map(int, input().split()))



    solve_puzzle(start, goal)

if __name__ == "__main__":
    main()
