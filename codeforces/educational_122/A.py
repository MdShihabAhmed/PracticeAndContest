def solver(n):
    if n%7==0:
        return n

    result = n-(n%7)
    if result//10==n//10:
        return result
    else:
        return result+7

    return k


t = int(input())

for _ in range(t):
    n = int(input())

    print(solver(n))