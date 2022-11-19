import sys

from itertools import permutations

def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')
    
    cows = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue'] 

    conditions = []
    for _ in range(int(input())):
        s = list(map(str,input().rstrip().split()))
        s =[s[0],s[-1]]
        conditions.append(s)
    
    allPossible = permutations(cows)

    for one in allPossible:
        for c in conditions:
            if abs(one.index(c[0])-one.index(c[1]))!=1:
                break
        else:
            print(*one,sep='\n')
            break



if __name__ == "__main__":
	solver('lineup')