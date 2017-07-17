import math
from decimal import *


def answer(str_n):
    tot = 0
    old_num = 0
    pattern = []
    i = 0
    # for i in xrange(1, str_n + 1):
    while i <= str_n:
        num = math.floor(i * math.sqrt(2))
        pattern.append(int(num))
        # print(i)
        # print"Num: ", num
        # print"Diff: ", num - old_num
        # print
        tot += num
        old_num = num
        i += 1
    # print(pattern)
    return int(tot)


# def test(n):
#     tot = 0
#     for i in xrange(1, n + 1):
#         tot += isqrt(2 * i * i)
#     return tot


def sqrt(num):
    res = 0
    bit = 1 << 328  # The second - to - top bit is set: 1 << 30 for 32 bits

    # "bit" starts at the highest power of four <= the argument.
    while bit > num:
        bit >>= 2

    while bit != 0:
        if num >= res + bit:
            num -= res + bit
            res = (res >> 1) + bit
        else:
            res >>= 1
        bit >>= 2
    return res


def isqrt(n):
    xn = 1
    xn1 = (xn + n / xn) / 2
    while abs(xn1 - xn) > 1:
        xn = xn1
        xn1 = (xn + n / xn) / 2
    while xn1 * xn1 > n:
        xn1 -= 1
    return xn1


def answer3(str_n):
    getcontext().prec = 1000
    alpha = Decimal(2).sqrt()
    n = int(str_n)
    m = Decimal(n * (alpha - 1)) // Decimal(1)
    tot = 0
    if n == 0:
        return tot
    else:
        tot = n * m + ((n * (n + 1)) / 2) - ((m * (m + 1)) / 2) - int(answer3(m))
        return str(tot)


def answer4(str_n):
    # alpha for this Beatty sequence is the sqrt(2). Alpha minus one expressed
    # as integer due to build up of float error in last program.
    alpha_min_one = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
    n = int(str_n)
    m = (alpha_min_one * n) // 10 ** 100  # "floors" value (sqrt(2) - 1 * n)
    tot = 0
    if n == 0:
        return tot
    else:
        tot = n * m + ((n * (n + 1)) / 2) - ((m * (m + 1)) / 2) - int(answer4(m))
        return str(tot)


print(answer(77))
# print(answer3("546812681195752981093125556779405341338292357723303109106442651602488249799843980805878294255763456"))
print(answer4("546812681195752981093125556779405341338292357723303109106442651602488249799843980805878294255763456"))
# print(sqrt(546812681195752981093125556779405341338292357723303109106442651602488249799843980805878294255763456))
# print(isqrt(100000))
# print(test(77))
# print(answer3("71907725394492636309172207631560989344719079157692262909372032463093070322200385253083390928963"
#              "01440844804555194855734306351590752576664899713897225578964975110715736994619411052088784049843"
#              "76477812331808340023075352602729369851525895652442163308948653402042738345192959788983753918865"
#              "219341425318496896548865"))
print(answer4("71907725394492636309172207631560989344719079157692262909372032463093070322200385253083390928963"
              "01440844804555194855734306351590752576664899713897225578964975110715736994619411052088784049843"
              "76477812331808340023075352602729369851525895652442163308948653402042738345192959788983753918865"
              "219341425318496896548865"))