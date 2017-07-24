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


PREV_STATE = {((0, 0), (0, 0)): 0,
              ((0, 0), (0, 1)): 1,
              ((0, 0), (1, 0)): 1,
              ((0, 0), (1, 1)): 0,
              ((0, 1), (0, 0)): 1,
              ((0, 1), (0, 1)): 0,
              ((0, 1), (1, 0)): 0,
              ((0, 1), (1, 1)): 0,
              ((1, 0), (0, 0)): 1,
              ((1, 0), (0, 1)): 0,
              ((1, 0), (1, 0)): 0,
              ((1, 0), (1, 1)): 0,
              ((1, 1), (0, 0)): 0,
              ((1, 1), (0, 1)): 0,
              ((1, 1), (1, 0)): 0,
              ((1, 1), (1, 1)): 0}
CUR_STATE = {0: (((0, 0), (0, 0)),
                 ((0, 0), (1, 1)),
                 ((0, 1), (0, 1)),
                 ((0, 1), (1, 0)),
                 ((0, 1), (1, 1)),
                 ((1, 0), (0, 1)),
                 ((1, 0), (1, 0)),
                 ((1, 0), (1, 1)),
                 ((1, 1), (0, 0)),
                 ((1, 1), (0, 1)),
                 ((1, 1), (1, 0)),
                 ((1, 1), (1, 1))),
             1: (((1, 0), (0, 0)),
                 ((0, 1), (0, 0)),
                 ((0, 0), (1, 0)),
                 ((0, 0), (0, 1)))}
COL_CACHE = {}


def get_col_comb(first, column):
    x = ((0, 0), (0, 1), (1, 0), (1, 1))
    count_possibility = []
    for key in first:
        nextCol = []
        for val in x:
            if PREV_STATE[((key[0], key[1]), val)] == column[0]:
                nextCol.append(val)
        for n in xrange(1, len(column)):
            newCol = []
            if len(nextCol) == 0:
                break
            for col in nextCol:
                for m in xrange(2):
                    tempCol = list(col)
                    if PREV_STATE[((key[n], key[n+1]), (col[n], m))] == column[n]:
                        tempCol.append(m)
                        newCol.append(tempCol)
            nextCol = newCol
        [count_possibility.append((key, tuple(c))) for c in nextCol]
    return tuple(count_possibility)


def swap_row_col(g):
    return tuple(zip(*g))


def first_col_int(col):
    x = ((0, 0), (0, 1), (1, 0), (1, 1))
    present = CUR_STATE[col[0]]
    for n in xrange(1, len(col)):
        new = []
        for z in present:  # Each prev state for current state
            for comb in x:  # Every combination of bottom row of prev state
                #  Retains only combinations yielding next state in column
                if PREV_STATE[(z[-1], comb)] == col[n]:
                    new.append(z[:]+(comb,))
        present = tuple(new)  # Builds column row by row
    return tuple([swap_row_col(x) for x in present])


def answer(g):
    rotation = swap_row_col(g)  # Transposes the grid
    first = {}
    right_grids = first_col_int(rotation[0])  # Builds first column of preimages
    COL_CACHE[rotation[0]] = right_grids
    for z in right_grids:  # For each valid state in the top grid
        if z[1] not in first:  # Puts all bottom rows in dict and counts number of instances of each
            first[z[1]] = 1
        else:
            first[z[1]] += 1
    for n in xrange(1, len(rotation)):
        second = {}
        if rotation[n] in COL_CACHE:
            newGrids = COL_CACHE[rotation[n]]
        else:
            newGrids = get_col_comb(first, rotation[n])  # Expands to next col to right in original grid/next down in transpose
            COL_CACHE[rotation[n]] = newGrids
        for z in newGrids:  # For each valid state in the bottom grid
            if z[0] in first:  # Checks for overlap between bottom row of state in 1st and top row of state in 2nd
                # Gives total number of states leading to particular bottom row of state in 2nd
                if z[1] in second:
                    second[z[1]] = first[z[0]] + second[z[1]]
                else:
                    second[z[1]] = first[z[0]]
        first = second
    return sum(first.itervalues())  # Returns total possibilities yielding all bottom row states in transposed grid

