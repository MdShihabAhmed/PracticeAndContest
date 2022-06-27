import sys
from math import factorial

for line in sys.stdin:
    n = int(line)
    result = factorial(n)

    if result>6227020800:
        print('Overflow!')
    elif result<10000:
        print('Underflow!')
    else:
        print(result)
    