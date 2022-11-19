
import sys

def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')

    #solve here
    n = int(input())

    positions = []
    for i in range(n):
        positions.append(int(input()))
    positions.sort()

    result = -5
    for i in range(n):
        j=k=positions[i]
        increment = 1
        difference = 1
        temp = 1
        while(j>=positions[0] and i-increment>=0):
            if j-difference>positions[i-increment]:
                break
            j-=difference
            tempI = increment
            while(i-increment>=0 and j<=positions[i-increment]):
                temp+=1
                increment+=1
                tempI = increment
            j=max(j-difference,positions[i-tempI+1])
            difference+=1

        increment = 1
        difference = 1
        while(k<=positions[-1] and i+increment<n):
            if k+difference<positions[i+increment]:
                break
            k+=difference
            tempI = increment
            while(i+increment<n and k>=positions[i+increment]):
                temp+=1
                increment+=1
                tempI = increment
            k=min(k+difference, positions[i+tempI-1])
            difference+=1
        if temp>=result:
            result = temp
    print(result)
    
if __name__ == "__main__":
    solver('angry')