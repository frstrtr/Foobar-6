"""
The Grandest Staircase Of Them All
==================================
With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order
to make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how
to build the best staircase EVER.
Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the
different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know
how many different types of staircases can be built with each amount of bricks, so she can pick the one with the most options.
Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step
must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total
amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and
the second step having a height of 1: (# indicates a brick)
#
##
21
When N = 4, you still only have 1 staircase choice:
#
#
##
31

But when N = 5, there are two ways you can build a staircase from the given bricks.
The two staircases can have heights (4, 1) or (3, 2), as shown below:
#
#
#
##
41
#
##
##
32
Write a function called answer(n) that takes a positive integer n and returns the number of different staircases that can
be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200,
because Commander Lambda's not made of money!
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
Test cases
==========
Inputs:
    (int) n = 3
Output:
    (int) 1
Inputs:
    (int) n = 200
Output:
    (int) 487067745
Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""


import unittest


class TestTheGrandestStaircaseOfThemAll(unittest.TestCase):
    def test_1(self):
        test_input = 3
        self.assertEqual(answer(test_input), 1)

    def test_2(self):
        test_input = 200
        self.assertEqual(answer(test_input), 487067745)


def answer(n):
    degeneracy = [0]*(n+1)
    degeneracy [0] = 1
    for i in range(1, n):
        for c in range (n, i-1, -1):
            degeneracy[c] += degeneracy[c-i]

    return degeneracy[n]


if __name__ == '__main__':
    unittest.main()
