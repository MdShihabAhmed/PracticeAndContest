import sys

def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')
    
    n = int(input())
    cows = list(map(int,input().split()))
    result = 0
    for i in range(n-1,0,-1):
        if cows[i]<cows[i-1]:
            result = i
            break
    print(result)

if __name__ == "__main__":
	solver('sleepy')