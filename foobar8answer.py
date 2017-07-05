'''
Expanding Nebula
================

You've escaped Commander Lambda's exploding space station along with numerous escape pods full of bunnies. But - oh no! - one of the escape pods has flown into a nearby nebula, causing you to lose track of it. You start monitoring the nebula, but unfortunately, just a moment too late to find where the pod went. However, you do find that the gas of the steadily expanding nebula follows a simple pattern, meaning that you should be able to determine the previous state of the gas and narrow down where you might find the pod.

From the scans of the nebula, you have found that it is very flat and distributed in distinct patches, so you can model it as a 2D grid. You find that the current existence of gas in a cell of the grid is determined exactly by its 4 nearby cells, specifically, (1) that cell, (2) the cell below it, (3) the cell to the right of it, and (4) the cell below and to the right of it. If, in the current state, exactly 1 of those 4 cells in the 2x2 block has gas, then it will also have gas in the next state. Otherwise, the cell will be empty in the next state.

For example, let's say the previous state of the grid (p) was:
.O..
..O.
...O
O...

To see how this grid will change to become the current grid (c) over the next time step, consider the 2x2 blocks of cells around each cell.  Of the 2x2 block of [p[0][0], p[0][1], p[1][0], p[1][1]], only p[0][1] has gas in it, which means this 2x2 block would become cell c[0][0] with gas in the next time step:
.O -> O
..

Likewise, in the next 2x2 block to the right consisting of [p[0][1], p[0][2], p[1][1], p[1][2]], two of the containing cells have gas, so in the next state of the grid, c[0][1] will NOT have gas:
O. -> .
.O

Following this pattern to its conclusion, from the previous state p, the current state of the grid c will be:
O.O
.O.
O.O

Note that the resulting output will have 1 fewer row and column, since the bottom and rightmost cells do not have a cell below and to the right of them, respectively.

Write a function answer(g) where g is an array of array of bools saying whether there is gas in each cell (the current scan of the nebula), and return an int with the number of possible previous states that could have resulted in that grid after 1 time step.  For instance, if the function were given the current state c above, it would deduce that the possible previous states were p (given above) as well as its horizontal and vertical reflections, and would return 4. The width of the grid will be between 3 and 50 inclusive, and the height of the grid will be between 3 and 9 inclusive.  The answer will always be less than one billion (10^9).

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (boolean) g = [[true, false, true], [false, true, false], [true, false, true]]
Output:
    (int) 4

Inputs:
    (boolean) g = [[true, false, true, false, false, true, true, true], [true, false, true, false, false, false, true, false], [true, true, true, false, false, false, true, false], [true, false, true, false, false, false, true, false], [true, false, true, false, false, true, true, true]]
Output:
    (int) 254

Inputs:
    (boolean) g = [[true, true, false, true, false, true, false, true, true, false], [true, true, false, false, false, false, true, true, true, false], [true, true, false, false, false, false, false, false, false, true], [false, true, false, false, false, false, true, true, false, false]]
Output:
    (int) 11567

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
'''

# SOLUTION

import time
import unittest
import random


def answer(g):
    start = time.time()
    a = [((True, False), (False, False)), ((False, True), (False, False)), ((False, False), (True, False)),
         ((False, False), (False, True))]

    b = [((False, False), (False, False)), ((True, True), (True, True))]
    b.extend((((True, True), (False, False)), ((False, False), (True, True)), ((True, False), (True, False)),
              ((False, True), (False, True))))
    b.extend((((True, True), (True, False)), ((True, False), (True, True)), ((False, True), (True, True)),
              ((True, True), (False, True))))
    b.extend((((True, False), (False, True)), ((False, True), (True, False))))

    agraph = {(False, True): [(False, False)], (True, False): [(False, False)],
              (False, False): [(True, False), (False, True)]}
    bgraph = {(False, True): [(False, True), (True, True), (True, False)],
              (True, False): [(True, False), (True, True), (False, True)],
              (False, False): [(False, False), (True, True)],
              (True, True): [(True, True), (False, False), (True, False), (False, True)]}

    for i in xrange(0, len(g[0])):
        for j in xrange(0, len(g) - 1):

            if g[j][i] == True:
                x = agraph
            else:
                x = bgraph
            if g[j + 1][i] == True:
                y = agraph
            else:
                y = bgraph

            column1 = {}
            for key in y:
                column1[key] = y[key]

            todel = []

            for botkey in column1:
                newmat = []
                for (ind, elem) in enumerate(column1[botkey]):
                    if j == 0:
                        if j == len(g) - 2:
                            if elem in x:
                                for k in x[elem]:
                                    newmat.append([k, elem, botkey])
                        else:
                            if elem in x:
                                for k in x[elem]:
                                    newmat.append([k, elem])
                    elif j == len(g) - 2:

                        if elem in column2:
                            for k in column2[elem]:
                                kk = []
                                for ind in k:
                                    kk.append(ind)
                                kk.append(elem)
                                kk.append(botkey)
                                newmat.append(kk)
                    else:
                        if elem in column2:
                            for k in column2[elem]:
                                kk = []
                                for ind in k:
                                    kk.append(ind)
                                kk.append(elem)
                                newmat.append(kk)

                if newmat == []:
                    todel.append(botkey)
                else:
                    column1[botkey] = newmat

            for key in todel:
                column1.pop(key, None)
            column2 = column1

        if i == 0:
            major = {}

            for key in column2:
                for (ind, elem) in enumerate(column2[key]):
                    q = tuple([row[1] for row in elem[:]])

                    if q in major:
                        major[q] += 1
                    else:
                        major[q] = 1

        elif i == len(g[0]) - 1:
            leftside = []
            major2 = {}
            for key in column2:
                for (ind, elem) in enumerate(column2[key]):
                    p = tuple([row[0] for row in elem[:]])
                    q = tuple([row[1] for row in elem[:]])

                    leftside.append(p)
                    if q in major2:
                        major2[q].append(p)
                    else:
                        major2[q] = [p]
            k = 0
            for key in major2:
                toadd = 0
                for (ind, elem) in enumerate(major2[key]):
                    if elem in major:
                        toadd += major[elem]
                        k += major[elem]
                major2[key] = toadd
        else:
            leftside = []
            major2 = {}
            for key in column2:
                for (ind, elem) in enumerate(column2[key]):
                    p = tuple([row[0] for row in elem[:]])
                    q = tuple([row[1] for row in elem[:]])

                    leftside.append(p)
                    if q in major2:
                        major2[q].append(p)
                    else:
                        major2[q] = [p]

            for key in major2:
                toadd = 0
                for (ind, elem) in enumerate(major2[key]):
                    if elem in major:
                        toadd += major[elem]
                major2[key] = toadd
            major = major2

    end = time.time()
    print(end - start)

    return k


def generate_binary_arry(height, width):
    random.seed(8675309)
    random.randint(0, 100)
    bin_arry = [[] for i in xrange(height)]
    for i in xrange(height):
        for j in xrange(width):
            bin_arry[i].append(random.randint(0, 100) % 2)
    return bin_arry


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

zero_arry = []
for i in xrange(9):
    zero_arry.append([])
    for j in xrange(20):
        zero_arry[i].append(0)
one_arry = []
for i in xrange(9):
    one_arry.append([])
    for j in xrange(50):
        one_arry[i].append(1)

simple = [[1, 1],
          [1, 1]]

test = generate_binary_arry(9, 10)

print answer(one_arry)