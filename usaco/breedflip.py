import sys

def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')
    
    n = int(input())
    A = input().rstrip()
    B = input().rstrip()

    r = 0
    for i in range(n):
        if B[i]==A[i]:
            result += r
            r = 0
        else:
            r = 1

if __name__ == "__main__":
	solver('breedflip')