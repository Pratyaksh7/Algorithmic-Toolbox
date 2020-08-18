
def lcs3(l1,l2,l3,n,m,l):
    if n == 0 or m == 0 or l == 0:
        return 0

    if t[n][m][l] != -1:
        return t[n][m][l]

    if l1[n-1] == l2[m-1] == l3[l-1]:
        t[n][m][l] = (1 + lcs3(l1,l2,l3,n-1,m-1,l-1))
        return t[n][m][l]

    else:
        # here we have to check all the possible pairs of least common sequence of 3 inputs , so 3! = 6 pairs
        # then find the max value from all those 6 pairs
        t[n][m][l] =  max(lcs3(l1,l2,l3,n,m-1,l-1) , lcs3(l1,l2,l3,n,m,l-1), lcs3(l1,l2,l3,n,m-1,l),
        lcs3(l1, l2, l3, n-1,m,l - 1), lcs3(l1,l2,l3,n-1,m,l),lcs3(l1, l2, l3, n-1, m - 1, l))

        return t[n][m][l]

n = int(input())
l1 = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))
l = int(input())
l3 = list(map(int, input().split()))

t = [[[-1 for k in range(l+1)] for j in range(m+1)] for i in range(n+1) ]
print(lcs3(l1,l2,l3,n,m,l))