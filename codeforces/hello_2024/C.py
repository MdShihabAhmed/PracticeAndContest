import sys

input = sys.stdin.readline

for _ in range(int(input())):
    l, r = map(int,input().split())
    temp = l^r
    temp = bin(temp)[2:]
    temp = max(0,32-len(temp))*"0"+temp

    k = 0
    for i in range(32):
        if temp[i]=="1":
            k=(31-i)
            break
    d = (2**k)-1 #all the bits below kth becomes 1
    
    # a consists of two parts now
    # one is l till the kth bit and the rests are 1s
    a = l|d 
    
    # b consists of three parts
    # one is l before the kth bit. kth bit is 1 and the rests are 0s
    b = a+1
    
    #a and b guarantees the max value now

    #c does not matter
    #just needs to be in the range
    
    for i in range(l,r+1):
        if i!=a and i!=b:
            c = i
            break
    
    print(a,b,c)
