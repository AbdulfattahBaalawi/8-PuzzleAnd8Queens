from collections import Counter


#start indexing row and colums to use a matrix of character
rows = 'ABCDEFGH'
cols = '12345678'



#intialize matrix by '0' character
board = {s: '-' for s in [row + col for row in rows for col in cols]}


#a goal function
def is_goal(state):
    queens = Counter(state.values())
    if queens['1'] != 8:
        return False
    return True




# general Search Algorithm
def search(state1, successors, is_goal):
    if is_goal(state1):
        return state1

    closedState = set()
    openStates = [state1]
    currentState = state1
    while ((len(openStates)!=0)&(not is_goal(currentState))):
        currentState = openStates.pop()
        exp = ''.join(list(currentState.values()))
        display_board(currentState)

        if exp not in closedState:
            closedState.add(exp)
            for state in successors(currentState):
                openStates.append(state)



    return False


def add_squares(state, s):
    start_row = rows.index(s[:1])
    start_col = cols.index(s[1:2])

    for k in state:
        if k != s and state[k] != 2:
            #check rows or columns
            if s[0] == k[0] or s[1] == k[1]:
                state[k] = '0'
                # check diagnal
            elif rows.index(k[0]) - cols.index(k[1]) == start_row - start_col:
                state[k] = '0'
                # check inverse diagnal
            elif rows.index(k[0]) + cols.index(k[1]) == start_row + start_col:
                state[k] = '0'
    return state

# find succesors states for the current state
def state_sucessors(state):
    # If there are not enough free spaces to place a queen it should return nothing
    values_count = Counter(state.values())
    #this if to check there no no space in the board
    if values_count['1'] + values_count['-'] < 8:
        return []

    states = []
    for s in state:
        if state[s] == '-':
            state2 = state.copy()
            state2[s] = '1'
            states.append(add_squares(state2, s))

    return states


def display_board(board):
    for r in rows:
        for c in cols:
            print(board[r + c], end=' '),
        print()
    print()


def solve_queens(puzzle):
    return search(puzzle, state_sucessors, is_goal)



##execution function
solve_queens(board)