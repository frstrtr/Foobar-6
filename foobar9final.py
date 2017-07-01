def answer(str_n):
    def int_sqrt(n):
        xn = 1
        xn1 = (xn + n / xn) / 2
        while abs(xn1 - xn) > 1:
            xn = xn1
            xn1 = (xn + n / xn) / 2
        while xn1 * xn1 > n:
            xn1 -= 1
        return xn1

    def calc_tot(n):
        tot = 0
        while n > 0:
            print(n)
            tot += sqrt(2 * n * n)
            n -= 1
        return tot

    def sqrt(num):
        res = 0
        bit = 1 << 8  # The second - to - top bit is set: 1 << 30 for 32 bits

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

    return calc_tot(int(str_n))

print(answer("11111111"))