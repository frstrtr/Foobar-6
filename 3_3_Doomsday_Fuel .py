"""
Doomsday Fuel
========================

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel.

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state). You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function answer(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly.

For example, consider the matrix m:

[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]

So, we can consider different paths to terminal states, such as:

s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5

Tracing the probabilities of each, we find that:

s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14

So, putting that together, and making a common denominator, gives an answer in the form of [s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is: [0, 3, 2, 9, 14].
Test cases

Inputs: (int) m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

Output: (int list) [7, 6, 8, 21]

Inputs: (int) m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

Output: (int list) [0, 3, 2, 9, 14]
"""

import unittest
import fractions
from fractions import Fraction


class TestDoomsdayFuel(unittest.TestCase):
    def test_1(self):
        test_input = [[0, 2, 1, 0, 0],
                      [0, 0, 0, 3, 4],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0]]
        self.assertEqual(answer(test_input), [7, 6, 8, 21])

    def test_2(self):
        test_input = [[0, 1, 0, 0, 0, 1],
                      [4, 0, 0, 3, 2, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0]]
        self.assertEqual(answer(test_input), [0, 3, 2, 9, 14])


def lcm(a, b):
    lcm_int = a * b // fractions.gcd(a, b)
    return lcm_int


def order_matrix(m, terminal_states):
    """
    Puts all terminal states at bottom of matrix. Returns matrix and dict of swaps from->to i.e {2:3, 3:2, 1:1,..etc
    """
    swaps = dict()
    ordered_m = []
    for i, val in enumerate(m):
        if i not in terminal_states:
            ordered_m.append(m[i])
            if not i == ordered_m.index(m[i]):
                swaps[i] = ordered_m.index(m[i])
    for i, val in enumerate(m):
        if i in terminal_states:
            ordered_m.append(m[i])
    return ordered_m, swaps


def find_terminals(m):
    terminal_states = []
    for i, row in enumerate(m):
        if sum(row) == 0:
            terminal_states.append(i)
    return terminal_states


def build_qr(m, terminal_states):
    q_matrix = [[] for n in xrange(len(m[0]) - len(terminal_states))]
    r_matrix = [[] for n in xrange(len(m[0]) - len(terminal_states))]
    index = 0
    for i, row in enumerate(m):
        for j, val in enumerate(row):
            if i not in terminal_states and j not in terminal_states:
                q_matrix[index].append(Fraction(val, sum(row)))
            elif i not in terminal_states:
                r_matrix[index].append(Fraction(val, sum(row)))
        if i not in terminal_states:
            index += 1

    return q_matrix, r_matrix


def fill_i_matrix(m):
    """
    Makes and fills square identity matrix of size m x m
    """
    i_matrix = []
    for i in xrange(0, m):
        i_matrix.append([])
        for j in xrange(0, m):
            if i == j:
                i_matrix[i].append(1)
            else:
                i_matrix[i].append(0)
    return i_matrix


def sub_matrices(m1, m2):
    """
    Subtract matrix m2 from matrix m1 and returns matrix m3
    """
    m3 = [[] for n in xrange(len(m1))]
    for i, row in enumerate(m1):
        for j, val in enumerate(m1):
            m3[i].append(m1[i][j] - m2[i][j])
    return m3


def mult_matrices(m1, m2):
    """
    Multiply matrix m1 by matrix m2 and return matrix m3.
    Throws error if multiplication not possible.
    """
    m3 = [[0 for n in xrange(len(m2[0]))] for i in xrange(len(m1))]  # len(m3) to match len m1
    assert len(m1[0]) == len(m2)  
    for i in xrange(len(m1)):  # row in m1
        for n in xrange(len(m2[0])):  # col in m2
            for j in xrange(len(m1[0])):  # col in m1
                m3[i][n] += (m1[i][j] * m2[j][n])
    return m3


def inverse_matrix(m):
    """
    Finds and returns inverse of matrix using row operations
    """
    inverse = [[0 for n in xrange(0, 2 * len(m))] for n in xrange(0, len(m))]
    for i in xrange(0, len(m)):
        for j in xrange(0, len(m)):
            inverse[i][j] = m[i][j]
    for i in xrange(0, len(m)):
        for j in xrange(len(m), 2 * len(m)):
            if i == j - len(m):
                inverse[i][j] = 1
            else:
                inverse[i][j] = 0
    for i in xrange(0, len(m)):
        for j in xrange(0, len(m)):
            if not i == j:
                proportion_flt = Fraction(inverse[j][i], inverse[i][i])
                for k in xrange(0, 2 * len(m)):
                    inverse[j][k] -= proportion_flt * inverse[i][k]

    for i in xrange(0, len(m)):
        a = inverse[i][i]
        for j in xrange(0, 2 * len(m)):
            inverse[i][j] /= a
    for i in xrange(0, len(m)):
        for j in xrange(0, len(m)):
            del inverse[i][0]

    return inverse


def answer(m):
    if m == [[0]]:  # Trivial yet is an anomaly to algorithm
        return [1, 1]

    terminal_states = find_terminals(m)
    q_matrix = build_qr(m, terminal_states)[0]
    r_matrix = build_qr(m, terminal_states)[1]
    inverse = inverse_matrix(
        sub_matrices(fill_i_matrix(len(q_matrix)), q_matrix))
    b_matrix = mult_matrices(inverse, r_matrix)
    lcm_int = 1
    if len(b_matrix) >= 1:
        for j in b_matrix[0]:
            lcm_int = lcm(lcm_int, j.denominator)
    else:
        for j in b_matrix:
            lcm_int = lcm(lcm_int, j.denominator)

    answer_matrix = []
    if len(b_matrix) >= 1:
        for j in b_matrix[0]:
            answer_matrix.append(j.numerator * (lcm_int // j.denominator))
        answer_matrix.append(lcm_int)
    else:
        for j in b_matrix:
            answer_matrix.append(j.numerator * (lcm_int // j.denominator))
        answer_matrix.append(lcm_int)
    return answer_matrix


if __name__ == '__main__':
    unittest.main()
