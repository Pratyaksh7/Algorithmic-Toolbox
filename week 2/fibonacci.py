# Uses python3
def calc_fib(n):
    arr = [1] * n
    result = [0, 1, 1]

    for i in range(2, n):
        arr[i] = arr[i-1] + arr[i-2]
        result.append(arr[i])

    return result[n]


n = int(input())
print(calc_fib(n))
