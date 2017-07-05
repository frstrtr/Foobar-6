"""
    Expanding Nebula
    ================
    You've escaped Commander Lambda's exploding space station along with numerous escape pods full of bunnies.
    But - oh no! - one of the escape pods has flown into a nearby nebula, causing you to lose track of it. You start
    monitoring the nebula, but unfortunately, just a moment too late to find where the pod went. However, you do find
    that the gas of the steadily expanding nebula follows a simple pattern, meaning that you should be able to determine
    the previous state of the gas and narrow down where you might find the pod.
    From the scans of the nebula, you have found that it is very flat and distributed in distinct patches, so you can
    model it as a 2D grid. You find that the current existence of gas in a cell of the grid is determined exactly by its
    4 nearby cells, specifically, (1) that cell, (2) the cell below it, (3) the cell to the right of it, and (4) the
    cell below and to the right of it. If, in the current state, exactly 1 of those 4 cells in the 2x2 block has gas,
    then it will also have gas in the next state. Otherwise, the cell will be empty in the next state.
    For example, let's say the previous state of the grid (p) was:
    .O..
    ..O.
    ...O
    O...
    To see how this grid will change to become the current grid (c) over the next time step, consider the 2x2 blocks of
    cells around each cell.  Of the 2x2 block of [p[0][0], p[0][1], p[1][0], p[1][1]], only p[0][1] has gas in it, which
    means this 2x2 block would become cell c[0][0] with gas in the next time step:
    .O -> O
    ..
    Likewise, in the next 2x2 block to the right consisting of [p[0][1], p[0][2], p[1][1], p[1][2]], two of the
    containing cells have gas, so in the next state of the grid, c[0][1] will NOT have gas:
    O. -> .
    .O
    Following this pattern to its conclusion, from the previous state p, the current state of the grid c will be:
    O.O
    .O.
    O.O
    Note that the resulting output will have 1 fewer row and column, since the bottom and rightmost cells do not have a cell below and to the right of them, respectively.
    Write a function answer(g) where g is an array of array of bools saying whether there is gas in each cell (the current scan of the nebula),
    Languages
    =========
    To provide a Python solution, edit solution.py
    To provide a Java solution, edit solution.java
    Test cases
    ==========
    Inputs:
        (boolean) g = [
                        [true, false, true],
                        [false, true, false],
                        [true, false, true]
                      ]
    Output:
        (int) 4
    Inputs:
        (boolean) g = [
                        [true, false, true, false, false, true, true, true],
                        [true, false, true, false, false, false, true, false],
                        [true, true, true, false, false, false, true, false],
                        [true, false, true, false, false, false, true, false],
                        [true, false, true, false, false, true, true, true]
                      ]
    Output:
        (int) 254
    Inputs:
        (boolean) g = [
                        [true, true, false, true, false, true, false, true, true, false],
                        [true, true, false, false, false, false, true, true, true, false],
                        [true, true, false, false, false, false, false, false, false, true],
                        [false, true, false, false, false, false, true, true, false, false]
                      ]
    Output:
        (int) 11567
"""
import unittest
import random

preimage_cache = dict()

# class Grid(object):
#     def __init__(self, grid = [[]]):
#         self.rows = [[a for a in grid[i]] for i in xrange(len(grid))]
#         self.cols = map(list, zip(*self.rows))
#     def __getitem__(self, (row, col)):
#         return self.rows[row][col]
# class PreStates(object):
#     def __init__(self, grid):
#         self.prestates = Grid()
#         if grid[i][j] == 1:
#             self.prestates.append(Grid([Grid([[1, 0], [0, 0]])],
#                                         [[0, 1], [0, 0]],
#                                         [[0, 0], [1, 0]],
#                                         [[0, 0], [0, 1]]]])
#         else:
#             self.prestates.append[Grid[[[[1, 1], [1, 1]],
#                                         [[1, 1], [1, 0]],
#                                         [[1, 1], [0, 1]],
#                                         [[0, 1], [1, 1]],
#                                         [[1, 0], [1, 1]],
#                                         [[1, 1], [0, 0]],
#                                         [[0, 1], [0, 1]],
#                                         [[0, 0], [1, 1]],
#                                         [[1, 0], [1, 0]],
#                                         [[0, 1], [1, 0]],
#                                         [[1, 0], [0, 1]],
#                                         [[0, 0], [0, 0]]]]]


def find_prev_states(state):
    """Takes the state of a cell and returns array of possible 2d arrays of states that lead to it"""
    if state == 1:
        return (((1, 0), (0, 0)),
                ((0, 1), (0, 0)),
                ((0, 0), (1, 0)),
                ((0, 0), (0, 1)))
    else:
        return (((1, 1), (1, 1)),
                ((1, 1), (1, 0)),
                ((1, 1), (0, 1)),
                ((0, 1), (1, 1)),
                ((1, 0), (1, 1)),
                ((1, 1), (0, 0)),
                ((0, 1), (0, 1)),
                ((0, 0), (1, 1)),
                ((1, 0), (1, 0)),
                ((0, 1), (1, 0)),
                ((1, 0), (0, 1)),
                ((0, 0), (0, 0)))


def find_col_states(grid):
    """ Takes a 2d array as input, expands it into its column vectors, and finds all preimages for each state in the
        column. Returns an array of all possible preimage states for each site in each column of the grid"""
    col_states = [[] for n in xrange(len(grid[0]))]  # Makes a spot for each column
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            col_states[j].append(find_prev_states(col))
    return tuple(col_states)


def compare_col_state(ary_1, ary_2 ):
    preimage_ary = []
    for state_1 in ary_1:
        for state_2 in ary_2:
            if state_1[-1] == state_2[0]:
                temp = list(state_1[:])
                temp.append(state_2[1])
                preimage_ary.append(temp)
    return tuple(preimage_ary)


def find_col_preimage(col):
    col_preimage = col[0]
    if len(col) == 1:
        return col[0]
    for i in xrange(len(col) - 1):
        col_preimage = compare_col_state(col_preimage, col[i+1])
    return tuple(col_preimage)

#
# def compare_col_preimages(col_1, col_2):  # Major slow down here...optimize
#     valid_preimages = []
#     for preimage_1 in col_1:
#         for preimage_2 in col_2:
#             cnt = 0
#             temp_preimages = []
#             for i, row in enumerate(preimage_1):
#                 temp_row = [preimage_2[i][1]]
#                 temp_preimages.append(temp_row)
#                 if row[-1] == preimage_2[i][0]:
#                     cnt += 1
#                 else:
#                     break
#             if cnt == len(preimage_2):
#                 valid_preimages.append(temp_preimages)
#
#     return valid_preimages


def transpose(arry):
    arry_t =  zip(*arry)
    return tuple(arry_t)


def compare_col_preimages(col_1, col_2):  # Major slow down here...optimize
    valid_preimages = []
    for preimage_1 in col_1:
        preimage_1_t = transpose(preimage_1)
        for preimage_2 in col_2:
            preimage_2_t = transpose(preimage_2)
            preimage_tup = ((preimage_1_t[0], preimage_1_t[1]), (preimage_2_t[0], preimage_2_t[1]))
            if preimage_tup in preimage_cache:
                valid_preimages.append(preimage_cache[preimage_tup])
            if preimage_1_t[-1] == preimage_2_t[0]:
                temp = preimage_1_t[-2], preimage_2_t[-1]
                valid_preimages.append(transpose(temp))
                preimage_cache[preimage_tup] = transpose(temp)
    return tuple(valid_preimages)



    # for state_1 in ary_1:
    #     for state_2 in ary_2:
    #         if state_1[-1] == state_2[0]:
    #             temp = state_1[:]
    #             temp.append(state_2[1])
    #             preimage_ary.append(temp)



def answer(g):
    if not len(g[0]): # Returns 0 in case of empty grid. Algorithm does not self check for emptiness
        return 0
    cols = find_col_states(g)
    next_preimages = find_col_preimage(cols[0])
    if len(cols) == 1:
        return len(next_preimages)
    for i in xrange(1, len(cols)):
        preimages = find_col_preimage(cols[i])
        next_preimages = compare_col_preimages(next_preimages, preimages)

    return len(next_preimages)


def generate_binary_arry(height, width):
    random.seed(8675309)
    random.randint(0, 100)
    bin_arry = [[] for i in xrange(height)]
    for i in xrange(height):
        for j in xrange(width):
            bin_arry[i].append(random.randint(0, 100) % 2)
    return bin_arry






class TestExpandingNebula(unittest.TestCase):
    def test1(self):
        test_input = [
                        [True, True, False, True, False, True, False, True, True, False],
                        [True, True, False, False, False, False, True, True, True, False],
                        [True, True, False, False, False, False, False, False, False, True],
                        [False, True, False, False, False, False, True, True, False, False]
                      ]
        self.assertEqual(answer(test_input), 11567)

    def test2(self):
        test_input = [
                        [True, False, True, False, False, True, True, True],
                        [True, False, True, False, False, False, True, False],
                        [True, True, True, False, False, False, True, False],
                        [True, False, True, False, False, False, True, False],
                        [True, False, True, False, False, True, True, True]
                      ]
        self.assertEqual(answer(test_input), 254)

    def test3(self):
        test_input = [
                        [True, False, True],
                        [False, True, False],
                        [True, False, True]
                      ]
        self.assertEqual(answer(test_input), 4)


# test_input = [
#                 [True, False, True],
#                 [False, True, False],
#                 [True, False, True]
#               ]

simple = [[1, 1, 1, 1]]

zero_arry = []
for i in xrange(25):
    zero_arry.append([])
    for j in xrange(1):
        zero_arry[i].append(0)

test_arry = generate_binary_arry(25, 1)

# col_states = find_col_states(zero_arry)
# print len(find_col_preimage(col_states[0]))

print(answer(simple))





