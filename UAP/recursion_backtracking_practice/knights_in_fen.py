import sys

input = sys.stdin.readline

def backtrack(arr, row, move):
    if move>=11:
        return move
    if row>=6:
        return
    start = row
    if row>1:
        start += 1
    
    for i in range(start, 5):
        if arr[row][i]=='0':
            backtrack(arr, row, move+1)
    

for _ in range(int(input())):
    board = []
    for i in range(5):
        board.append(list(input().rstrip()))
