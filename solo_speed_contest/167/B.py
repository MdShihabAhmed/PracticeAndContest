import sys

input = sys.stdin.readline


a, b = map(int,input().split())
print("#"*(b+2))
for i in range(a):
    s = input().rstrip()
    print("#",s,"#",sep="")
print("#"*(b+2))