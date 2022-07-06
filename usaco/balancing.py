import sys

def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')

    n, b = map(int,input().split())
    cowLocations = []
    for i in range(n):
        x, y = map(int,input().split())
        cowLocations.append((x,y))
    
    result = float('inf')
    for i in range(n):
        for j in range(n):
            first = 0
            second = 0
            third = 0
            fourth = 0
            for k in range(n):
                if cowLocations[i][0]>=cowLocations[k][0] and cowLocations[j][1]>=cowLocations[k][1]:
                    first+=1
                elif cowLocations[i][0]<cowLocations[k][0] and cowLocations[j][1]>=cowLocations[k][1]:
                    second+=1
                elif cowLocations[i][0]<cowLocations[k][0] and cowLocations[j][1]<cowLocations[k][1]:
                    third+=1
                else:
                    fourth+=1

            temp = max(first,second,third,fourth)
            result = min(result,temp)

    
    print(result)

if __name__ == "__main__":
	solver('balancing')