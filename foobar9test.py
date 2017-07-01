import math

def answer(str_n):
    sqrt_2 = 1.41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157273501384623091229702492483605585073721264412149709993583141322266592750559275579995050115278206057147010955997160597027453459

    tot = 0
    old_num = 0
    pattern = []
    i = 0
    # for i in xrange(1, str_n + 1):
    while i <= str_n:
        num = math.floor(i * sqrt_2)
        #pattern.append(int(num))
        #print(i)
        # print"Num: ", num
        # print"Diff: ", num - old_num
        # print
        tot += num
        #old_num = num
        i += 1
    # print(pattern)
    return int(tot)


def test(n):
    tot = 0
    for i in xrange(1, n + 1):
        tot += isqrt(2 * i * i)
    return tot


def sqrt(num):
    res = 0
    bit = 1 << 328 # The second - to - top bit is set: 1 << 30 for 32 bits

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

def answer2(str_n):
    sqrt_2 = 1.41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157273501384623091229702492483605585073721264412149709993583141322266592750559275579995050115278206057147010955997160597027453459
    # div_2 = Number.from_str('0.5')
    # one = Number.from_str('1')
    #
    # n = Number.from_str(str_n)
    #
    # # Approximation which will give the right result +/-1
    candidate_str = (sqrt_2 * str_n * (str_n + 1) - str_n) / 2
    return candidate_str

print(answer(111111111))
print
print(int(round(answer2(111111111),0)))
#print(sqrt(546812681195752981093125556779405341338292357723303109106442651602488249799843980805878294255763456))
#print(isqrt(100000))
#print(test(77))
