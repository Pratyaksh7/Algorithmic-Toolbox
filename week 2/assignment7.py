# using python3
# Last Digit of the Sum of Fibonacci Numbers Again

def SumFib(n, m):
    if m > n:
        m, n = n, m
    result = []
    for i in range(0, n+1):
        if i <= 1:
            result.append(i)
        else:
            result.append(result[i-1] + result[i-2])

    add = 0
    for i in range(m, n+1):
        add += result[i]

    return (add % 10)


n, m = map(int, input().split())
print(SumFib(n, m))
