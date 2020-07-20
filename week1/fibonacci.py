import time


def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))


result = fibo(int(input()))
t1 = time.time()
print(result)
t2 = time.time()

print("Ececution time is: ", t2-t1)
