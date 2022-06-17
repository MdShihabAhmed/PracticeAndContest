from collections import Counter

def solver(filename):
    input = open(filename+'.in', 'r').readline
    fout = open(filename+'.out', 'w')
    print = lambda x: fout.write(str(x)+'\n')

    board = []
    result = [0]*3
    for i in range(3):
        board.append(list(input().rstrip()))

    for i in range(3):
        result[len(Counter(board[i]))-1]+=1
        temp = [board[0][i],board[1][i],board[2][i]]
        result[len(Counter(temp))-1]+=1

    temp = [board[0][0],board[1][1],board[2][2]]
    result[len(Counter(temp))-1]+=1

    temp = [board[0][2],board[1][1],board[2][0]]
    result[len(Counter(temp))-1]+=1
    
    print(result[0]) 
    print(result[1]) 




if __name__ == "__main__":
	solver('tttt')