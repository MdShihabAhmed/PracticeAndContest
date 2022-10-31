import sys

def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')
    
    x,y,z = list(map(int,input().split()))

    if z-y==1 and y-x==1:
        print(0)
    elif z-y==2 or y-x==2:
        print(1)
    else:
        print(2)

    print(max(z-y,y-x)-1)
    
if __name__ == "__main__":
	solver('herding')