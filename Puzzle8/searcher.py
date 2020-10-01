from node import *
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



    def generalSearch(self,step):
        """Run general search algorthim"""
        #TODO: Implement breadth first search
        queue = [self.start]

        #this is the visited means the closed states
        visited = set()
        found = False
        state=start

        # the queue means the open states
        while (len(queue)!=0)&(state != self.goal):
            step += 1    # count the steps
            state = queue.pop()
            if state in visited:
                continue
            visited.add(state)
            for s in state.next():
                queue.insert(0, s)
            if state == self.goal:
                found=state
        if found:
            self.print_path(state)
            print("Find solution")
            print("the steps taken to find the solution: %s" % step)
        else:
            print("No solution found")




#the main function
if __name__ == "__main__":
    #Unit test
    print("Search for solution\n")
    #intialized state from class node
    start = Node([1,0,2,5,4,3,8,7,6])

    #intialized goal from class node
    goal = Node([1,2,3,4,5,6,7,8,0])

# use a general search algorithm
    search = Searcher(start, goal)
    step=0
    search.generalSearch(step)

    print("Elabse Time untill find a solution: %s" % elapsed)
