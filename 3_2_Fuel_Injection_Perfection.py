"""
Fuel Injection Perfection
=========================
Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP
doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage
while you're at it - so you took the job gladly.
Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need
to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out
the most efficient way to sort and shift the pellets down to a single pellet at a time.
The fuel control mechanisms have three operations:
1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is
cut in half, the safety controls will only allow this to happen if there is an even number of pellets)
Write a function called answer(n) which takes a positive integer as a string and returns the minimum number of operations
needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits
long, so there won't ever be more pellets than you can express in that many digits.
For example:
answer(4) returns 2: 4 -> 2 -> 1
answer(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
Test cases
==========
Inputs:
    (string) n = "4"
Output:
    (int) 2
Inputs:
    (string) n = "15"
Output:
    (int) 5
Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""


import unittest

class TestTheGrandestStaircaseOfThemAll(unittest.TestCase):
    def test_1(self):
        test_input = "4"
        self.assertEqual(answer(test_input), 2)

    def test_2(self):
        test_input = "15"
        self.assertEqual(answer(test_input), 5)

    def test_torture(self):
        test_input = "71907725394492636309172207631560989344719079157692262909372032463093070322200385253083390928963" \
                     "01440844804555194855734306351590752576664899713897225578964975110715736994619411052088784049843" \
                     "76477812331808340023075352602729369851525895652442163308948653402042738345192959788983753918865" \
                     "219341425318496896548865"  # (2^1026) + 1 which is 100 digits long
        self.assertEqual(answer(test_input), 1027)


def answer(n):
    """
    checks for and applies operation leading to most consecutive 0's in bin(n) using property that x&(x-1) replaces
    leftmost 1 in bin(x) with a 0
    """
    n = int(n)
    cnt = 0
    while n != 1:
        if not n & 1:
            n >>= 1
        # checks if n+1 will give more consecutive 0's than n-1. Only true when leftmost bits in n are of form "111".
        # "011" or "001" makes n-1 preferred operation
        elif (n & (n+1)) <= ((n-1) & (n-2)):
            n += 1
        elif n == 3:  # 3 is anomaly and requires hard code
            n -= 1
        else:
            n -= 1
        cnt += 1
    return cnt



if __name__ == '__main__':
    unittest.main()
