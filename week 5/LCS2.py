
def lcs(l1,l2,n,m):
    if n == 0 or m == 0:
        return 0
    if t[n][m] != -1:
        return t[n][m]

    if l1[n-1] == l2[m-1] :
        # storing the recursive value in the t matrix for future values of recursive calls
        t[n][m]= (1+ lcs(l1,l2,n-1,m-1))
        return t[n][m]
    else:
        t[n][m] = max(lcs(l1,l2,n,m-1),lcs(l1,l2,n-1,m))
        return t[n][m]

n = int(input())
l1 = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

#memoization : initializing a matrix with -1 then updating its value on recursive call
t = [[-1 for j in range(m+1)] for i in range(n+1) ]      # m and n should be incremented my 1 to access index m and n i.e., t[n][m]
print(lcs(l1,l2,n,m))