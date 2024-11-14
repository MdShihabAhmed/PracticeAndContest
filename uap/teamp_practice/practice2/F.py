n = int(input())
s = input()

stack = []

result = 0
for c in s:
    if c=='(':
        stack.append(c)
        continue
    if stack:
        if (c==')'):
            stack.pop()
            result+=2
print(result)