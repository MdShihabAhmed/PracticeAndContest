
import sys

def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')

    #solve here
    n = int(input())
    a = []
    for i in range(n):
        a.append(tuple(map(int,input().split())))
    
    a.sort()
    result = 0
    
    for i in range(n):
        result+=max(0,a[i][0]-result)+a[i][1]
    
    print(result)
    
if __name__ == "__main__":
    solver('cowqueue')