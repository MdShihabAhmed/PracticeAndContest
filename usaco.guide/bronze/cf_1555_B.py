#1555/B
import sys

input = sys.stdin.readline

def solver(W, H, x1, y1, x2, y2, w, h):
    if (max(x1,W-x2)>=w) or (max(y1,H-y2)>=h):
        return 0
    if not ((x1+W-x2)>=w or (y1+H-y2)>=h):
        return -1

    minH = float('inf')
    minW = float('inf')
    if (x1+W-x2)>=w:
        minW = (w-max(x1,W-x2))
    if (y1+H-y2)>=h:
        minH = (h-max(y1, H-y2))
        
    return min(minH,minW)

for _ in range(int(input())):
    W, H = map(int,input().split())
    x1, y1, x2, y2 = map(int,input().split())
    w, h = map(int,input().split())
    print(solver(W, H, x1, y1, x2, y2, w, h))