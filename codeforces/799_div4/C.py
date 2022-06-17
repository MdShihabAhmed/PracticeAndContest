import sys
    
input = sys.stdin.readline

def solver(s):
    flag = False
    for i in range(1,7):
        for j in range(1,7):
            if s[i][j]=='#':
                    if s[i-1][j-1]=='#' and s[i-1][j+1]=='#' and s[i+1][j-1]=='#' and s[i+1][j+1]=='#':
                        print(i+1, j+1)
                        return

    return result
for _ in range(int(input())):
    s = []
    _ = input()
    for i in range(8):
        s.append(input().rstrip())
    
    solver(s)