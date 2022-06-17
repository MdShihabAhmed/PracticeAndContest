import sys,math
    
input = sys.stdin.readline
    
def solver(n, brackets):
    c = 0
    stack = []
    for b in brackets:
        if stack == []:
            stack.append(b)
        else:
            if stack[0] == '(' or b == ')':
                stack.clear()
                c+=1
            else:
                stack.append(b)

    print(c, len(stack))
    
for _ in range(int(input())):
    n = int(input())
    brackets = input().rstrip()
    
    solver(n, brackets)