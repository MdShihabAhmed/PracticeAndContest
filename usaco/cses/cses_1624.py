import sys

board = []

for _ in range(8):
    s = input().rstrip()
    board.append(list(s))

column = [0]*8

diagonal1 = [0]*15
diagonal2 = [0]*15

result = 0
def solver(row):
    global result
    if row==8:
        result+=1
        return
    for j in range(8):
        if board[row][j]=='*' or (column[j] or diagonal1[row+j] or diagonal2[7-(row-j)]):
            continue
        column[j] = 1
        diagonal1[row+j] = 1
        diagonal2[7-(row-j)] = 1
        solver(row+1)
        column[j] = 0
        diagonal1[row+j] = 0
        diagonal2[7-(row-j)] = 0


solver(0)
print(result)