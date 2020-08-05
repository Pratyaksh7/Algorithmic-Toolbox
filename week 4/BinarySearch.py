def binarySearch(arrA, low, high, x):
    while low <= high:
        mid = int((low+high)/2)

        if arrA[mid] == x:
            return mid
        elif arrA[mid] < x:
            l = mid+1
        else:
            r = mid-1

    return -1


A = list(map(int, input().split()))
n = A[0]
arrA = A[1:]
B = list(map(int, input().split()))
k = B[0]
arrB = B[1:]

output = []

for i in range(k):
    result = binarySearch(arrA, 0, len(arrA)-1, arrB[i])
    output.append(result)

print(output)
