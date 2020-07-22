# python 3

def GCD(a, b):
    if b == 0:
        return a
    else:
        mod = a % b
    return (GCD(b, mod))


a, b = map(int, input().split())
print(GCD(a, b))
