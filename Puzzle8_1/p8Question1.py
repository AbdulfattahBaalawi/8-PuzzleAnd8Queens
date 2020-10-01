from Puzzle_8_node import *
from time import time

class Searcher(object):
    """Searcher that manuplate searching process."""

    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def print_path(self, state):
        path = []
        while state:
            path.append(state)
            state = state.prev
        path.reverse()
        print("\n-->\n".join([str(state) for state in path]))

    # teration_Limit if we dont have a solution
    def SearchAlgorithm(self, iteration_Limit = 200000):
        """Run general search algorithm search."""
        #TODO: Implement breadth first search
        Openstates = [self.start]

        #this is the Closed_states means the closed states
        Closed_states = set()
        reached_the_goal = False
        state=start

        # the Openstates means the open states


        while (len(Openstates)!=0)&(state != self.goal):
            state = Openstates.pop()
            if state in Closed_states:
                continue
            Closed_states.add(state)
            for s in state.next():
                Openstates.insert(0, s)
            if state == self.goal:
                reached_the_goal=state
        if reached_the_goal:
            self.print_path(state)
            print("Find solution")
        else:
            print("No solution found")







#the main function
if __name__ == "__main__":
    #Unit test
    print("Search for solution\n")
    #intialized state from class node
    start = Puzzle_8_node([2,0,1,4,5,3,8,7,6])

    #intialized goal from class node
    goal = Puzzle_8_node([1,2,3,4,5,6,7,8,0])

# use a general search algorithm
    search = Searcher(start, goal)

    #store start time to variable start time
    start_time = time()
    search.SearchAlgorithm()

    # store start time  to varuiable end time
    end_time = time()
    #to calculate the taken time form start to end and stor it in elabsed time
    elapsed = end_time - start_time
    print("Search time: %s" % elapsed)
    print("Number of initialized node: %d" % Puzzle_8_node.n)
