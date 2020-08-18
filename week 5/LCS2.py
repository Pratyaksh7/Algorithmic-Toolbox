def lcs(l1,l2,n,m):
    if n == 0 or m == 0:
        return 0
    if l1[n-1] == l2[m-1] :
        return (1+ lcs(l1,l2,n-1,m-1))
    else:
        return max(lcs(l1,l2,n,m-1),lcs(l1,l2,n-1,m))

n = int(input())
l1 = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

print(lcs(l1,l2,n,m))