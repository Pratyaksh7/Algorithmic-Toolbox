# using python3
import random


def partition3(arr, l, r):
    lt = l
    gt = r
    i = l
    pivot = arr[l]

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt


def randomized_quick_sort(arr, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    arr[l], arr[k] = arr[k], arr[l]

    m1, m2 = partition3(arr, l, r)
    randomized_quick_sort(arr, l, m1-1)
    randomized_quick_sort(arr, m2+1, r)


n, arr = int(input()), list(map(int, input().split()))
randomized_quick_sort(arr, 0, n-1)
for i in arr:
    print(i, end=' ')
