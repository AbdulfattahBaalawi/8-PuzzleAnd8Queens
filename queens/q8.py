from collections import Counter


#start indexing row and colums to use a matrix of character
rows = 'ABCDEFGH'
cols = '12345678'

#intialize matrix by '0' character
chess_board = {s: '0' for s in [row + col for row in rows for col in cols]}

#a goal function
def is_it_equal_goal(state):
    queens = Counter(state.values())
    if queens['Q'] != 8:
        return False
    return True




# general Search Algorithm
def general_search_search(state1, successors, is_it_equal_goal):
    if is_it_equal_goal(state1):
        return state1

    closedState = set()
    openStates = [state1]
    currentState = state1
    while ((len(openStates)!=0)&(not is_it_equal_goal(currentState))):
        currentState = openStates.pop()
        exp = ''.join(list(currentState.values()))
        display_board(currentState)

        if exp not in closedState:
            closedState.add(exp)
            for state in successors(currentState):
                openStates.append(state)
    return False

#this function for adding available place
def add_place(state, s):
    start_row = rows.index(s[:1])
    start_col = cols.index(s[1:2])

    for k in state:
        if k != s and state[k] != 2:
            if s[0] == k[0] or s[1] == k[1]:
                state[k] = 'X'
            elif rows.index(k[0]) - cols.index(k[1]) == start_row - start_col:
                state[k] = 'X'
            elif rows.index(k[0]) + cols.index(k[1]) == start_row + start_col:
                state[k] = 'X'
    return state


def sucessors(state):
    # If there are not enough free spaces to place a queen it should return nothing
    values_count = Counter(state.values())
    if values_count['Q'] + values_count['0'] < 8:
        return []

    states = []
    for s in state:
        if state[s] == '0':
            state2 = state.copy()
            state2[s] = 'Q'
            states.append(add_place(state2, s))

    return states

#display board function
def display_board(board):
    for r in rows:
        for c in cols:
            print(board[r + c], end=' '),
        print()
    print()


def find_sulotion(puzzle):
    return general_search_search(puzzle, sucessors, is_it_equal_goal)



##execution function
find_sulotion(chess_board)