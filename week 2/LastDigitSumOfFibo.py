# python 3
def SumFib(n):
    result = []
    for i in range(0, n+1):
        if i <= 1:
            result.append(i)
        else:
            result.append(result[i-1] + result[i-2])
    return (sum(result) % 10)


print(SumFib(int(input())))
