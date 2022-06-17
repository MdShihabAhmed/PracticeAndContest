import sys

input = sys.stdin.readline

def solver(n,arr):
    maxSoFar = maxEndingHere = subsequence = arr[0]

    for i in arr[1:]:
        maxEndingHere = max(maxEndingHere+i,i)
        maxSoFar = max(maxSoFar, maxEndingHere)
        subsequence = max(subsequence+i,subsequence,i)
    
    return maxSoFar,subsequence

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    print(*solver(n, arr))