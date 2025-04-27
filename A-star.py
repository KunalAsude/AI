def print_board(elements):
    for i in range(9):
        if i % 3 == 0:
            print()
        print("_" if elements[i] == -1 else elements[i], end=" ")
    print()

def heuristic(start, goal):
    h = 0
    for i in range(9):
        if start[i] != -1:
            goal_pos = goal.index(start[i])
            h += abs(goal_pos // 3 - i // 3) + abs(goal_pos % 3 - i % 3)
    return h

def moveleft(state, pos):
    state[pos], state[pos - 1] = state[pos - 1], state[pos]

def moveright(state, pos):
    state[pos], state[pos + 1] = state[pos + 1], state[pos]

def moveup(state, pos):
    state[pos], state[pos - 3] = state[pos - 3], state[pos]

def movedown(state, pos):
    state[pos], state[pos + 3] = state[pos + 3], state[pos]

def movetile(start, goal):
    empty_at = start.index(-1)
    row, col = empty_at // 3, empty_at % 3

    # Create copies for all possible moves
    t1, t2, t3, t4 = start[:], start[:], start[:], start[:]
    f1, f2, f3, f4 = float('inf'), float('inf'), float('inf'), float('inf')

    if col - 1 >= 0:
        moveleft(t1, empty_at)
        f1 = heuristic(t1, goal)
    if col + 1 < 3:
        moveright(t2, empty_at)
        f2 = heuristic(t2, goal)
    if row - 1 >= 0:
        moveup(t3, empty_at)
        f3 = heuristic(t3, goal)
    if row + 1 < 3:
        movedown(t4, empty_at)
        f4 = heuristic(t4, goal)

    # Choose the best move based on the heuristic
    min_heuristic = min(f1, f2, f3, f4)

    if f1 == min_heuristic:
        moveleft(start, empty_at)
    elif f2 == min_heuristic:
        moveright(start, empty_at)
    elif f3 == min_heuristic:
        moveup(start, empty_at)
    elif f4 == min_heuristic:
        movedown(start, empty_at)

def solve_eight(start, goal, g=0):
    g += 1
    movetile(start, goal)
    print_board(start)

    if start == goal:
        print(f"Solved in {g} moves.")
        return

    solve_eight(start, goal, g)

def main():
    start = []
    goal = []

    print("Enter the start state (use -1 for the blank space):")
    for _ in range(9):
        start.append(int(input()))

    print("Enter the goal state (use -1 for the blank space):")
    for _ in range(9):
        goal.append(int(input()))

    print("\nInitial Board:")
    print_board(start)

    print("\nSolving...\n")
    solve_eight(start, goal)

if __name__ == '__main__':
    main()
