"""
# Dodge the Lasers!
# =================

# Oh no! You've managed to escape Commander Lambdas collapsing space station in an escape pod with the rescued bunny prisoners - but Commander Lambda isnt about to let you get away that easily. She's sent her elite fighter pilot squadron after you - and they've opened fire!

# Fortunately, you know something important about the ships trying to shoot you down. Back when you were still Commander Lambdas assistant, she asked you to help program the aiming mechanisms for the starfighters. They undergo rigorous testing procedures, but you were still able to slip in a subtle bug. The software works as a time step simulation: if it is tracking a target that is accelerating away at 45 degrees, the software will consider the targets acceleration to be equal to the square root of 2, adding the calculated result to the targets end velocity at each timestep. However, thanks to your bug, instead of storing the result with proper precision, it will be truncated to an integer before adding the new velocity to your current position.  This means that instead of having your correct position, the targeting software will erringly report your position as sum(i=1..n, floor(i*sqrt(2))) - not far enough off to fail Commander Lambdas testing, but enough that it might just save your life.

# If you can quickly calculate the target of the starfighters' laser beams to know how far off they'll be, you can trick them into shooting an asteroid, releasing dust, and concealing the rest of your escape.  Write a function answer(str_n) which, given the string representation of an integer n, returns the sum of (floor(1*sqrt(2)) + floor(2*sqrt(2)) + ... + floor(n*sqrt(2))) as a string. That is, for every number i in the range 1 to n, it adds up all of the integer portions of i*sqrt(2).

# For example, if str_n was "5", the answer would be calculated as
# floor(1*sqrt(2)) +
# floor(2*sqrt(2)) +
# floor(3*sqrt(2)) +
# floor(4*sqrt(2)) +
# floor(5*sqrt(2))
# = 1+2+4+5+7 = 19
# so the function would return "19".

# str_n will be a positive integer between 1 and 10^100, inclusive. Since n can be very large (up to 101 digits!), using just sqrt(2) and a loop won't work. Sometimes, it's easier to take a step back and concentrate not on what you have in front of you, but on what you don't.
"""


import unittest


class TestDodgeTheLasers(unittest.TestCase):
    def test_1(self):
        test_input = "5"
        self.assertEqual(answer(test_input), "19")

    def test_2(self):
        test_input = "77"
        self.assertEqual(answer(test_input), "4208")

    def test_torture(self):
        test_input = "71907725394492636309172207631560989344719079157692262909372032463093070322200385253083390928963" \
                     "01440844804555194855734306351590752576664899713897225578964975110715736994619411052088784049843" \
                     "76477812331808340023075352602729369851525895652442163308948653402042738345192959788983753918865" \
                     "219341425318496896548865"  # (2^1026) + 1 which is 100 digits long
        self.assertEqual(answer(test_input), "3656251862507334448148179357411972294813205338243570072399608556509885357"
                                             "2501592156627075023977411067341589424590108494452342577069275381301528664"
                                             "8713467314724409580700486858456282969735344383354280498317253684972423688"
                                             "0399137190063559454262133821524826418317800715699648839069268323667413740"
                                             "3742614331223435935402453035423695823538445283290619837000290506129738885"
                                             "5837817678284818646327428940940798745085837091696852308958883678563866545"
                                             "5192211168001061493525287792007324647921921998049795017289928866989976959"
                                             "3068942778535840280145136631201950415699342212774262487665784007034469384"
                                             "2275855344226240937331812480075580")


def answer(str_n):
    # alpha for this Beatty sequence is the sqrt(2). Alpha minus one expressed
    # as integer due to build up of float error in last program.
    alpha_min_one = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
    n = int(str_n)
    m = (alpha_min_one * n) // 10 ** 100  # "floors" value (sqrt(2) - 1 * n)
    tot = 0
    if n == 0:
        return tot
    else:
        tot = n * m + ((n * (n + 1)) / 2) - ((m * (m + 1)) / 2) - int(answer(m))
        return str(tot)


if __name__ == '__main__':
    unittest.main()