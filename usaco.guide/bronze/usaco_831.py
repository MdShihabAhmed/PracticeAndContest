
import sys

def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')

    #solve here
    board = []

    for i in range(3):
        board.append(input().rstrip())

    result = []
    for i in range(3):
        result.append(set(([board[0][i],board[1][i],board[2][i]])))
        result.append(set(([board[i][0],board[i][1],board[i][2]])))
        if i==1:
            continue
    result.append(set(([board[0][0],board[1][1],board[2][2]])))
    result.append(set(([board[2][0],board[1][1],board[0][2]])))

    one = 0
    two = 0

    for i in range(len(result)):
        if len(result[i])>2:
            continue
        elif len(result[i])>1:
            two+=1
        else:
            one+=1
        for j in range(i+1,len(result)):
            if result[i]==result[j]:
                result[j]={'A','B','C'}
    print(one)
    print(two)
if __name__ == "__main__":
    solver('tttt')