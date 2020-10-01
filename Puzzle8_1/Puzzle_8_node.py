#Author: _ here she should put her name
# this is a classs for a Puzzle_8_node  what we mean by a node is board state
# this class is very important for moving nodes in the board
# the important function for moving nodes are here
import heapq

class Puzzle_8_node(object):
    """
    Represent state of board in 8 puzzle problem.
    """
    # start with zero
    n = 0


# make the node like a linked list each state has previous state


    def __init__(self, board, prev_state = None):

        #add 9 places
        assert len(board) == 9

        self.board = board[:];
        self.prev = prev_state
        self.step = 0
        #increment the number of node with one
        Puzzle_8_node.n += 1



#increment predecessor
        if self.prev:
            self.step = self.prev.step + 1

    def __eq__(self, other):
        """Check wether two state is equal."""
        return self.board == other.board

    def __hash__(self):
        """Return hash code of object.
        what i meant is that the board has a size of 3
        the first line h[0]  contains 0 ,1,2
        the first line h[1]  contains 3 ,4,5
        the first line h[2]  contains 6,7,8



        Used for comparing elements in set
        """
        h = [0, 0, 0]
        h[0] = self.board[0] << 6 | self.board[1] << 3 | self.board[2]
        h[1] = self.board[3] << 6 | self.board[4] << 3 | self.board[5]
        h[2] = self.board[6] << 6 | self.board[7] << 3 | self.board[8]

        h_val = 0
        for h_i in h:
            h_val = h_val * 31 + h_i

        return h_val

    def __str__(self):
        string_list = [str(i) for i in self.board]
        sub_list = (string_list[:3], string_list[3:6], string_list[6:])
        return "\n".join([" ".join(l) for l in sub_list])




    def next(self):
        """Return next states from this state."""
        next_moves = []
        i = self.board.index(0)

        next_moves = (self.move_up(i), self.move_down(i), self.move_left(i), self.move_right(i))

        return [s for s in next_moves if s]




    # moving node right

    def move_right(self, i):
        x, y = self.__i2pos(i)
        if y < 2:
            right_state = Puzzle_8_node(self.board, self)
            right = self.__pos2i(x, y+1)
            right_state.__swap(i, right)
            return right_state

    # moving node left
    def move_left(self, i):
        x, y = self.__i2pos(i)
        if y > 0:
            left_state = Puzzle_8_node(self.board, self)
            left = self.__pos2i(x, y - 1)
            left_state.__swap(i, left)
            return left_state



 # moving node up

    def move_up(self, i):
        x, y = self.__i2pos(i)
        if x > 0:
            up_state = Puzzle_8_node(self.board, self)
            up = self.__pos2i(x - 1, y)
            up_state.__swap(i, up)
            return up_state

    def move_down(self, i):
        x, y = self.__i2pos(i)
        if x < 2:
            down_state = Puzzle_8_node(self.board, self)
            down = self.__pos2i(x + 1, y)
            down_state.__swap(i, down)
            return down_state



#swap between node
    def __swap(self, i, j):
        self.board[j], self.board[i] = self.board[i], self.board[j]

    def __i2pos(self, index):
        return (int(index / 3), index % 3)

    def __pos2i(self, x, y):
        return x * 3 + y


class PriorityQueue:
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        # FIXME: restored old behaviour to check against old results better
        # FIXED: restored to stable behaviour
        entry = (priority, self.count, item)
        # entry = (priority, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0