import sys

def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')

    #solve here
    milk = [list(map(int,input().split())) for i in range(3)]
    
    for i in range(100):
        temp = min(milk[(i+1)%3][0]-milk[(i+1)%3][1],milk[(i)%3][1])
        milk[(i)%3][1]-=temp
        milk[(i+1)%3][1]+=temp

    for i in range(3):
        print(milk[i][1])

if __name__ == "__main__":
	solver('mixmilk')