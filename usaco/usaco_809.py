import sys

def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')
    
    n = int(input())
    breakout = list(map(int,input().split()))
    
    flag = False
    if breakout[0]>0:
        flag = True
    else:
        breakout[0] = 0
    
    m = M = 0
    temp = -1
    for i in range(n-1,-1,-1):
        if breakout[i]>0 and temp == breakout[i]:
            flag = True
            break
        if breakout[i] > 0:
            temp = breakout[i]
        elif breakout[i] == 0:
            temp = breakout[i]
            m += 1
            M += 1
        else:
            if temp <= 0:
                M += 1
                temp = breakout[i]
            elif temp == 1:
                m += 1
                M += 1
                temp = breakout[i]
            else:
                temp -= 1
    if flag:
        print(-1)
    else:
        print(m, M)
if __name__ == "__main__":
	solver('taming')