import sys
input = sys.stdin.readline

def solver(l, r, a):
    if a>r:
        return r

    if r//a>l//a:
        return max((r//a+r%a),((r//a)-1)+a-1)
    return r//a + r%a
   
for _ in range(int(input())):
    l, r, a = map(int,input().split())

    print(solver(l, r, a))