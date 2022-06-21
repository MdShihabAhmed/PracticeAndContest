for _ in range(int(input())):
    sprinklers = list(input())

    letters = [0]*26
    stack = []
    stack.append(sprinklers[0])

    for i in range(1,len(sprinklers)-1):
        if stack[-1]==sprinklers[i]:
            letters[ord(stack[-1])-65]+=1
            stack.pop()
            letters[ord(stack[-1])-65]+=1
        else:
            stack.append(sprinklers[i])
    print('Case',_+1)
    for i in range(26):
        if letters[i]!=0:
            print(chr(i+65),'=',letters[i])