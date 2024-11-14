import sys

input = sys.stdin.readline

def checkHorizon(grid, i,j, c):
    if j>3:
        return False
    if grid[i][j]==c and grid[i][j+1]==c and grid[i][j+2]==c and grid[i][j+3]==c:
        return (4*(5-i+1),7*(5-i+1))
    return False

def checkVertical(grid, i,j, c):
    if i<3:
        return False
    if grid[i][j]==c and grid[i-1][j]==c and grid[i-2][j]==c and grid[i-3][j]==c:
        temp = 5-i+4
        return (temp,(temp)*7)
    return False

def checkDiagonal(grid, i,j, c):
    if i<3 or j>3:
        return False
    if grid[i][j]==c and grid[i-1][j+1]==c and grid[i-2][j+2]==c and grid[i-3][j+3]==c:
        temp = (5-i+1)
        temp1 = 10
        return (temp*4+temp1,(5-i+4)*7)
    return False


for test in range(int(input())):
    input()
    grid = []
    for i in range(6):
        temp = input().strip()
        grid.append(list(temp))
    cMin = float('inf')
    fMin = float('inf')
    cMax = float('-inf')
    fMax = float('-inf')

    for i in range(5,-1,-1):
        for j in range(7):
            temp = checkHorizon(grid,i,j,'C')
            if temp:
                cMin = min(cMin,temp[0])
                cMax = max(cMax,temp[1])
            temp = checkVertical(grid,i,j,'C')
            if temp:
                cMin = min(cMin,temp[0])
                cMax = max(cMax,temp[1])
            temp = checkDiagonal(grid,i,j,'C')
            if temp:
                cMin = min(cMin,temp[0])
                cMax = max(cMax,temp[1])
            
            temp = checkHorizon(grid,i,j,'F')
            if temp:
                fMin = min(fMin,temp[0])
                fMax = max(fMax,temp[1])
            temp = checkVertical(grid,i,j,'F')
            if temp:
                fMin = min(fMin,temp[0])
                fMax = max(fMax,temp[1])
            temp = checkDiagonal(grid,i,j,'F')
            if temp:
                fMin = min(fMin,temp[0])
                fMax = max(fMax,temp[1])

    # print(cMin,cMax)
    # print(fMin,fMax)
    result = 0
    if cMin==float('inf') or fMin == float('inf'):
        if cMin<fMin:
            result = 'C'
        elif cMin>fMin:
            result = 'F'
        else:
            result = '0'
    elif cMin==fMin or cMax==fMax:
        result = '?'
    elif cMin<fMin or cMax<fMax:
        result = 'C'
    elif fMin<cMin or fMax<cMax:
        result = 'F'
    print(f"Case #{test+1}: {result}")