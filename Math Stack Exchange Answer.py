import random
import time

box = {((0, 0), (0, 0)): 0,
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

COL_CACHE = {}


def get_col_comb(first,column):
    x = ((0,0),(0,1),(1,0),(1,1))
    count_possibility = []

    for key in first:
        nextCol = []

        for val in x:
            if box[((key[0],key[1]),val)] == column[0]:
                nextCol.append(val)

        for n in xrange(1,len(column)):
            newCol = []
            if len(nextCol) == 0:
                break
            for col in nextCol:
                for m in xrange(2):
                    tempCol = list(col)
                    if box[((key[n],key[n+1]),(col[n],m))] == column[n]:
                        tempCol.append(m)
                        newCol.append(tempCol)
            nextCol = newCol
        [count_possibility.append((key,tuple(c))) for c in nextCol]
    return tuple(count_possibility)


def swap_row_col(g):
    return tuple(zip(*g))


def initialize(col):
    g0 = col[0]
    l = []
    for key, val in box.iteritems():
        if g0 == val:
            l.append(key)
    return tuple(l)


def first_col_int(f_c_col):
    x = ((0, 0), (0, 1), (1, 0), (1, 1))
    present = initialize(f_c_col)
    for n in xrange(1, len(f_c_col)):
        new = []
        for z in present:  # Each prev state for current state
            for comb in x:
                possibility = (z[n], comb)
                if box[possibility] == f_c_col[n]:
                    temp = list(z)
                    temp.append(comb)
                    new.append(temp)
        present = tuple(new)
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
            newGrids = get_col_comb(first, rotation[n])  # Expands to next col to right
            COL_CACHE[rotation[n]] = newGrids
        for z in newGrids:  # For each valid state in the bottom grid
            if z[0] in first:  # Checks for overlap between bottom row of state in 1st and top row of state in
                # Gives total number of states leading to particular bottom row of state in second
                if z[1] in second:
                    second[z[1]] = first[z[0]] + second[z[1]]
                else:
                    second[z[1]] = first[z[0]]
        first = second
    return sum(first.itervalues())  # Returns total possibilities yielding all bottom row states in transposed grid


def generate_binary_arry(height, width):
    random.seed(8675309)
    random.randint(0, 100)
    bin_arry = [[] for i in xrange(height)]
    for i in xrange(height):
        for j in xrange(width):
            bin_arry[i].append(random.randint(0, 100) % 2)
    return bin_arry


cell_1 = [[1, 0, 1],
          [0, 1, 0],
          [1, 0, 1]]

cell_2 = [[1, 1, 1, 1, 1, 1]]

cell_3 = [[0],
          [0],
          [0],
          [0],
          [0],
          [0],
          [0],
          [0],
          [0]]


cell_4 = [[1, 1],
          [1, 1]]


cell_5 = [[1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]


zero_arry = []
for i in xrange(9):
    zero_arry.append([])
    for j in xrange(50):
        zero_arry[i].append(0)

one_arry = []
for i in xrange(7):
    one_arry.append([])
    for j in xrange(50):
        one_arry[i].append(1)

test_arry = generate_binary_arry(10, 51)


grid = []
for i in xrange(len(test_arry)-1):
    grid.append([])
    for j in xrange(len(test_arry[0])-1):
        if sum([test_arry[i][j], test_arry[i+1][j], test_arry[i][j+1], test_arry[i+1][j+1]]) == 1:
            grid[i].append(1)
        else:
            grid[i].append(0)

start = time.time()
print answer(grid)
print time.time()-start
# print
# print len(first_col_int(swap_row_col(test_arry)[0]))
