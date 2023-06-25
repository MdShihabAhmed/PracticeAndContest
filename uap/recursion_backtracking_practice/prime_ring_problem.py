from sys import stdin

primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

def ring(n, check, arr):
    if len(arr)>=n:
        if arr[-1]+1 in primes:
            print(" ".join([str(i) for i in arr]))
        return
    for i in range(1, n+1):
        if not check[i] and arr[-1]+i in primes:
            check[i] = True
            arr.append(i)
            ring(n, check, arr)
            check[i] = False
            arr.pop()

cnt = 0
for line in stdin:
    n = int(line)
    check = [False]*(n+1)
    arr = [1]
    check[1] = True
    if cnt:
        print()
    cnt+=1
    print(f"Case {cnt}:")
    ring(n, check, arr)
