# using python3
A = list(map(int, input().split()))
n = A[0]
arrA = A[1:]
B = list(map(int, input().split()))
k = B[0]
arrB = B[1:]

indexes = {arrA[i]: i for i in range(n)}
for i in range(k):
    if arrB[i] in indexes:
        print(indexes.get(arrB[i]), end=' ')
    else:
        print(-1, end=' ')
