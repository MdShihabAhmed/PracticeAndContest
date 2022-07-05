import sys

def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')
    
    crossingPoints = input().rstrip()
    result = 0
    temp = [0]*52
    for i in range(52):
        for j in range(i+1,52):
            if crossingPoints[i]==crossingPoints[j]:
                temp[i] = j
                break
    
    for i in range(52):
        for j in range(i+1,temp[i]):
            if temp[i]<temp[j]:
                result+=1

    print(result)
if __name__ == "__main__":
	solver('circlecross')