import numpy as np

file = open("data/day4.txt")
file_contents = file.read()
contents_split = file_contents.splitlines()

to_cross = contents_split[0].split(',')
boards_els = contents_split[2:]
boards_els.append('')
boards = []
board = []

def add_boards(boards_els):
    x = 0
    while x < len(boards_els)-1:
        board, i = add_board(boards_els[x:])
        boards.append(board)
        x += i
    return

def add_board(_boards_els):
    i = 0
    el = _boards_els[i]
    board = []
    while el != '':
        board.append([x for x in el.split(' ') if x.isnumeric()])
        i += 1
        el = _boards_els[i]
    i += 1
    return board, i

add_boards(boards_els)
win = False
crossed = {}
for i in range(len(boards)):
    crossed[i] = [[0, 0], []]

w_n = 0
winning_board = None
for num in to_cross:
    for board in range(len(boards)):
        b = np.array(boards[board])
        crossed[board][1].extend(np.argwhere(b == num))
        rows = [x[0] for x in crossed[board][1]]
        cols = [x[1] for x in crossed[board][1]]
        row_max = crossed[board][0][0]
        col_max = crossed[board][0][1]
        for r, c in zip(rows, cols):
            if rows.count(r) > row_max:
                row_max = rows.count(r)
            if cols.count(c) > col_max:
                col_max = cols.count(c)
        crossed[board][0][0] = row_max
        crossed[board][0][1] = col_max
        if crossed[board][0][0] == 5 or crossed[board][0][1] == 5:
            winning_board = b
            winning_board_ix = board
            win = True
            break
    if win:
        w_n = num
        break

# sum of all unmarked numbers in the board
print(winning_board)
marked_numbers_ix = np.array(crossed[winning_board_ix][1])
rows = marked_numbers_ix[:,0]
cols = marked_numbers_ix[:,1]
marked_numbers = winning_board[rows, cols]

unmarked_numbers = []
for row in range(5):
    for col in range(5):
        if winning_board[row][col] not in marked_numbers:
            unmarked_numbers.append(int((winning_board[row][col])))

answer = sum(unmarked_numbers)*int(w_n)
print(answer)










