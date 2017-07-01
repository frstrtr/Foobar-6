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
import itertools

preimage_cache = dict()

def transpose(arry):
    return map(list, zip(*arry))


def build_state_array(grid):
    state_arry = []
    for i, row in enumerate(grid):
        state_arry.append([])
        for col in row:
            if col == 1:
                state_arry[i].append([[[1, 0], [0, 0]],
                                      [[0, 1], [0, 0]],
                                      [[0, 0], [1, 0]],
                                      [[0, 0], [0, 1]]])
            else:
                state_arry[i].append([[[1, 1], [1, 1]],
                                      [[1, 1], [1, 0]],
                                      [[1, 1], [0, 1]],
                                      [[0, 1], [1, 1]],
                                      [[1, 0], [1, 1]],
                                      [[1, 1], [0, 0]],
                                      [[0, 1], [0, 1]],
                                      [[0, 0], [1, 1]],
                                      [[1, 0], [1, 0]],
                                      [[0, 1], [1, 0]],
                                      [[1, 0], [0, 1]],
                                      [[0, 0], [0, 0]]])
    return state_arry


def is_valid_col_state(st_1, st_2):
    return st_1[-1] == st_2[0]


def is_valid_row_state(st_1, st_2):
    st_1_t = transpose(st_1)
    st_2_t = transpose(st_2)
    return st_1[-1] == st_2[0]


def is_valid_adjacent_state(st_1, st_2):
    return st_1[-1][-1] == st_2[0][0]


def find_valid_col_states(col):
    valid_col_states = col[0]
    for i in xrange(len(col) - 1):
        temp_col_states = []
        for state_1 in valid_col_states:
            for state_2 in col[i + 1]:
                 if is_valid_col_state(state_1, state_2):
                    temp_col_states.append((state_1[:] + state_2[1:]))
        valid_col_states = temp_col_states
    return valid_col_states


def find_valid_row_states(row):
    valid_row_states = row[0]
    for i in xrange(len(row) - 1):
        temp_row_states = []
        for state_1 in valid_row_states:
            for state_2 in row[i + 1]:
                if is_valid_row_state(state_1, state_2):
                    temp_row_states.append((state_1[:] + state_2[1:]))
        valid_row_states = temp_row_states
    return valid_row_states


def find_valid_adjacency_states(cell):
    valid_adjacency_states = []
    for state_1 in cell[1][0]:
        for state_2 in cell[1][1]:
            if is_valid_col_state(state_1, state_2):
                valid_adjacency_states.append((state_1, state_2))
    return valid_adjacency_states

def generate_binary_arry(height, width):
    random.seed(8675309)
    random.randint(0, 100)
    bin_arry = [[] for i in xrange(height)]
    for i in xrange(height):
        for j in xrange(width):
            bin_arry[i].append(random.randint(0, 100) % 2)
    return bin_arry


def answer(g):
    return

# class TestExpandingNebula(unittest.TestCase):
#     def test1(self):
#         test_input = [
#                         [True, True, False, True, False, True, False, True, True, False],
#                         [True, True, False, False, False, False, True, True, True, False],
#                         [True, True, False, False, False, False, False, False, False, True],
#                         [False, True, False, False, False, False, True, True, False, False]
#                       ]
#         self.assertEqual(answer(test_input), 11567)
# 
#     def test2(self):
#         test_input = [
#                         [True, False, True, False, False, True, True, True],
#                         [True, False, True, False, False, False, True, False],
#                         [True, True, True, False, False, False, True, False],
#                         [True, False, True, False, False, False, True, False],
#                         [True, False, True, False, False, True, True, True]
#                       ]
#         self.assertEqual(answer(test_input), 254)
# 
#     def test3(self):
#         test_input = [
#                         [True, False, True],
#                         [False, True, False],
#                         [True, False, True]
#                       ]
#         self.assertEqual(answer(test_input), 4)


cell_1 = [[1, 0, 1],
          [0, 1, 0],
          [1, 0, 1]]

cell_2 = [[1, 1],
          [1, 1]]

cell_3 = [[1, 1],
          [0, 1]]

cell_4 = [[1, 1],
          [1, 1]]


zero_arry = []
for i in xrange(1):
    zero_arry.append([])
    for j in xrange(7):
        zero_arry[i].append(0)

test_arry = generate_binary_arry(9, 10)

print(answer(zero_arry))

st_arry = build_state_array(cell_1)
st_arry_t = transpose(st_arry)

# for row in st_arry:
#     print row
valid_cols = []
for col in st_arry_t:
    valid_cols.append(find_valid_col_states(col))
find_valid_row_states()
vld_col_sts = find_valid_col_states(st_arry_t[0])
vld_row_sts = find_valid_row_states(st_arry[0])
vld_adj_sts = find_valid_adjacency_states(st_arry)
print vld_col_sts
print len(vld_col_sts)
print
print vld_row_sts
print len(vld_row_sts)
print


