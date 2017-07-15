"""
Don't Get Volunteered!
======================
As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!
To help yourself get to and from your bunk every day, write a function called answer(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:
-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
Test cases
==========
Inputs:
    (int) src = 19
    (int) dest = 36
Output:
    (int) 1
Inputs:
    (int) src = 0
    (int) dest = 1
Output:
    (int) 3
constraints.txt: Python
======
Your code will run inside a Python 2.7.6 sandbox.
Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.
"""


def answer(src, dest):
    board = []
    for i in range(0, 8):
        board.append([])
        for n in range(0, 8):
            board[i].append(0)

    src_cord = (src % 8, src // 8)
    dest_cord = (dest % 8, dest // 8)
    cords = [src_cord]

    found_point = False
    moves_cnt = 0

    if src_cord == dest_cord:
        return 0

    def allowed_moves(cords): # takes list of coordinates
        moves = []
        for  cord in cords:
            if cord[0] + 1 < 8: # x+1, y+2
                if cord[1] + 2 < 8:
                    if board[cord[1] + 2][cord[0] + 1] == 0:
                        board[cord[1] + 2][cord[0] + 1] == 1
                        if (cord[0] + 1, cord[1] + 2) == dest_cord:
                            return (True, [])
                        moves.append((cord[0] + 1, cord[1] + 2))

            if cord[0] + 1 < 8: # x+1, y-2
                if cord[1] - 2 > -1:
                    if board[cord[1] - 2][cord[0] + 1] == 0:
                        board[cord[1] - 2][cord[0] + 1] == 1
                        if (cord[0] + 1, cord[1] - 2) == dest_cord:
                            return (True, [])
                        moves.append((cord[0] + 1, cord[1] - 2))

            if cord[0] - 1 > -1: # x-1, y+2
                if cord[1] + 2 < 8:
                    if board[cord[1] + 2][cord[0] - 1] == 0:
                        board[cord[1] + 2][cord[0] - 1] == 1
                        if (cord[0] - 1, cord[1] + 2) == dest_cord:
                            return (True, [])
                        moves.append((cord[0] - 1, cord[1] + 2))

            if cord[0] - 1 > -1: # x-1, y-2
                if cord[1] - 2 > -1:
                    if board[cord[1] - 2][cord[0] - 1] == 0:
                        board[cord[1] - 2][cord[0] - 1] == 1
                        if (cord[0] - 1, cord[1] - 2) == dest_cord:
                            return (True, [])
                        moves.append((cord[0] - 1, cord[1] - 2))

            if cord[0] + 2 < 8:  # x+2, y+1
                if cord[1] + 1 < 8:
                    if board[cord[1] + 1][cord[0] + 2] == 0:
                        board[cord[1] + 1][cord[0] + 2] == 1
                        if (cord[0] + 2, cord[1] + 1) == dest_cord:
                            return (True, [])
                        moves.append((cord[0] + 2, cord[1] + 1))

            if cord[0] + 2 < 8:  # x+2, y-1
                if cord[1] - 1 > -1:
                    if board[cord[1] - 1][cord[0] + 2] == 0:
                        board[cord[1] - 1][cord[0] + 2] == 1
                        if (cord[0] + 2, cord[1] - 1) == dest_cord:
                            return (True, [])
                        moves.append((cord[0] + 2, cord[1] - 1))

            if cord[0] - 2 > -1:  # x-2, y+1
                if cord[1] + 1 < 8:
                    if board[cord[1] + 1][cord[0] - 2] == 0:
                        board[cord[1] + 1][cord[0] - 2] == 1
                        if (cord[0] - 2, cord[1] + 1) == dest_cord:
                            return (True, [])
                        moves.append((cord[0] - 2, cord[1] + 1))

            if cord[0] - 2 > -1:  # x-2, y-1
                if cord[1] - 1 > -1:
                    if board[cord[1] - 1][cord[0] - 2] == 0:
                        board[cord[1] - 1][cord[0] - 2] == 1
                        if (cord[0] - 2, cord[1] - 1) == dest_cord:
                            return (True, [])
                        moves.append((cord[0] - 2, cord[1] - 1))
        return (False, moves)

    while not found_point:
        found_point, cords = allowed_moves(cords)
        moves_cnt += 1

    return moves_cnt



print(answer(0,1))