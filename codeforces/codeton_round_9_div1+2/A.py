import sys
from collections import Counter
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    result = [i*2+1 for i in range(n)]
    
    print(" ".join(map(str,result)))