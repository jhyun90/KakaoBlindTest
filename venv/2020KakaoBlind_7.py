# 2020 Kakao Blind Recruitment - 7

board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

start = board[0][0:2]
print(start)

start_left_idx = 0
start_right_idx = 1

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[start_right_idx + 1] == 0:
            start_right_idx += 1

        else:


        # if board[start_left_idx - 1] == 0:
        #     start_left_idx += 1

    if board[i + 1][start_left_idx] == 0 and board[start_right_idx] == 0:
        start_left_idx += 1
        start_right_idx += 1

    if board[i + 1][start_left_idx] == 0 and board[i + 1][start_right_idx] == 0:
        start_left_idx += 1
        board[start_left_idx, start_right_idx] = board[start_left_idx, ]
