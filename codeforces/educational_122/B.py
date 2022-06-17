def solver(s):
    zero = s.count('0')
    one = len(s)-zero
    if zero<one:
        return zero
    elif one<zero:
        return one
    else:
        return zero-1


t = int(input())

for _ in range(t):
    s = input()

    print(solver(s))