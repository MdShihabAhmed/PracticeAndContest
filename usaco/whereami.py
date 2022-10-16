
import sys

def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')

    #solve here
    n = int(input())
    s = input().rstrip()

    temp = set()

    for i in range(n):
        temp.clear()
        for j in range(n-i):
            temp.add(s[j:j+i+1])
        if len(temp)==(n-i):
            print(i+1)
            break


if __name__ == "__main__":
    solver('whereami')