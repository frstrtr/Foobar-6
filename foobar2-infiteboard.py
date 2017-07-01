import math

def answer(src, dest):

    index_x = abs(dest_x - src_x)
    index_y = abs(dest_y - src_y)

    x = index_x
    y = index_y
    if x < y:
        temp = x
        x = y
        y = temp
    d = x - y
    if x == 1 and y == 0:
        return 3
    elif x == 1 and y == 1:
        return 4
    #elif x == 2 and y == 2:
        #return  4
    elif y > d:
        return d + 2 * math.floor((-d + y) / 3)
    else:
       return   d - 2 * math.floor((d - y) / 4)
