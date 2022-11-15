import sys
from collections import defaultdict

def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')
    
    states = defaultdict(lambda: defaultdict(int))
    result = 0

    for i in range(int(input())):
        city, state = input().split()
        city = city[:2]
        if city==state:
            continue
        if state in states[city]:
            result+=states[city][state]
        states[state][city]+=1

    print(result)
if __name__ == "__main__":
	solver('citystate')