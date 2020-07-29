# using python3
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
products = []
while len(a) > 0:
    maxA = max(a)
    maxB = max(b)
    products.append(maxA * maxB)
    a.remove(maxA)
    b.remove(maxB)

print(sum(products))
