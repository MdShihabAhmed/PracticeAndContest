import sys

def solver(filename):
    sys.stdin = open(filename + '.in', 'r')
    sys.stdout = open(filename + '.out', 'w')
    
    n, m = map(int,input().split())
    spottyCow = []
    plainCow = []
    for i in range(n):
        spottyCow.append(input().rstrip())
    
    for i in range(n):
        plainCow.append(input().rstrip())

    result = 0
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(spottyCow[j][i])
        flag = False
        for j in range(n):
            if plainCow[j][i] in temp:
                flag = True
                break
        if not flag:
            result+=1
    
    print(result)


if __name__ == "__main__":
	solver('cownomics')