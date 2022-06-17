import sys

n = int(sys.stdin.readline())

while True:
    sys.stdout.write(str(n)+' ')
    if n==1:
        break
    elif n%2:
        n=n*3+1
    else:
        n//=2