# using python3
import sys
input = sys.stdin.readline()

m = int(input)
count = 0
while m != 0:
    if m >= 10:
        m -= 10
        count += 1
    elif m < 10 and m >= 5:
        m -= 5
        count += 1
    elif m < 5 and m >= 1:
        m -= 1
        count += 1

print(count)
