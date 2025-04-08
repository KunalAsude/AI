g = 0  # global cost from start (g(n))

# Function to display the board
def print_board(elements):
    for i in range(9):
        if i % 3 == 0:
            print()
        if elements[i] == -1:
            print("_", end=" ")
        else:
            print(elements[i], end=" ")
    print()

# Manhattan Distance Heuristic + g(n)
def heuristic(start, goal):
    global g
    h = 0
    for i in range(9):
        if start[i] == -1:
            continue
        goal_pos = goal.index(start[i])
        h += abs(goal_pos // 3 - i // 3) + abs(goal_pos % 3 - i % 3)
    return h + g

# Movement functions
def moveleft(state, pos):
    state[pos], state[pos - 1] = state[pos - 1], state[pos]

def moveright(state, pos):
    state[pos], state[pos + 1] = state[pos + 1], state[pos]

def moveup(state, pos):
    state[pos], state[pos - 3] = state[pos - 3], state[pos]

def movedown(state, pos):
    state[pos], state[pos + 3] = state[pos + 3], state[pos]

# Function to move the blank tile in the best direction
def movetile(start, goal):
    empty_at = start.index(-1)
    row = empty_at // 3
    col = empty_at % 3

    # Create copies for all 4 possible moves
    t1 = start[:]
    t2 = start[:]
    t3 = start[:]
    t4 = start[:]
    f1 = f2 = f3 = f4 = float('inf')

    if col - 1 >= 0:
        moveleft(t1, empty_at)
        f1 = heuristic(t1, goal)
    if col + 1 < 3:
        moveright(t2, empty_at)
        f2 = heuristic(t2, goal)
    if row + 1 < 3:
        movedown(t3, empty_at)
        f3 = heuristic(t3, goal)
    if row - 1 >= 0:
        moveup(t4, empty_at)
        f4 = heuristic(t4, goal)

    # Choose the best (minimum f(n))
    min_heuristic = min(f1, f2, f3, f4)

    if f1 == min_heuristic:
        moveleft(start, empty_at)
    elif f2 == min_heuristic:
        moveright(start, empty_at)
    elif f3 == min_heuristic:
        movedown(start, empty_at)
    elif f4 == min_heuristic:
        moveup(start, empty_at)

# Recursive A* solve
def solveEight(start, goal):
    global g
    g += 1
    movetile(start, goal)
    print_board(start)
    f = heuristic(start, goal)

    if f == g:
        print("Solved in {} moves".format(f))
        return

    solveEight(start, goal)

# Main function
def main():
    global g
    start = []
    goal = []

    print("Enter the start state (use -1 for empty tile):")
    for _ in range(9):
        start.append(int(input()))

    print("Enter the goal state (use -1 for empty tile):")
    for _ in range(9):
        goal.append(int(input()))

    print("\n Initial Board:")
    print_board(start)
    print("\n Solving...\n")
    solveEight(start, goal)

# Run the program
if __name__ == '__main__':
    main()
