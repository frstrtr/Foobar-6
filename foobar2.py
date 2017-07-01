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

    return moves_cnt, cords



print(answer(0,63))