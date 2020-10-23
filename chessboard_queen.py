board = []
for i in range(8):
    board.append(input())
cols , diag1 , diag2 = [0] * 8 , [0] * 15 , [0] * 15
cnt = 0
def backtrack(r):
    global cnt, cols , diag1 , diag2
    if r == 8:
        cnt += 1
        return
    for c in range(8):
        if board[r][c] =='*' or cols[c] or diag1[r + c] or diag2[r - c+7]:
            continue
        cols[c] = diag1[r+c] = diag2[r-c+7] = 1
        backtrack(r + 1)
        cols[c] = diag1[r + c] = diag2[r - c + 7] = 0


backtrack(0)
print(cnt)
