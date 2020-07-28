# using python3
n = int(input())
list1 = list(map(int, input().split()))
singles = []
doubles = []
for i in list1:
    if i <= 9:
        singles.append(i)
    else:
        doubles.append(i)

singles.sort(reverse=True)
doubles.sort(reverse=True)
result = singles + doubles
result = [str(i) for i in result]
string = ""
for i in result:
    string += i

print(string)


# Input:
# 5
# 9 4 6 1 9
# Output:
# 99641
