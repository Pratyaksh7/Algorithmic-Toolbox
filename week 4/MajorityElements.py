# using python3
from collections import Counter
n, arr = int(input()), list(map(int, input().split()))
count = Counter(arr)
values = []

for key, value in count.items():
    values.append(value)

if max(values) > n/2:
    print(1)
else:
    print(0)
