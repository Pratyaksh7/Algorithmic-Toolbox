# using python3

def gold(weights,n,W):
    if W == 0 or n == 0:       # Base Condition
        return 0

    if t[n][W] != 0:
        return t[n][W]

    if weights[n-1] <= W:
        # max(if weights of bars of gold is selected, if not selected)
        t[n][W] = max(weights[n-1] + gold(weights,n-1,W-weights[n-1]), gold(weights, n-1, W))
        return t[n][W]

    else:
        # if Weight of bar of gold is greater than the capacity W then only reduce the size of the weights array
        t[n][W] = gold(weights,n-1,W)
        return t[n][W]

W,n = list(map(int,input().split()))
weights = list(map(int,input().split()))
t = [[0 for j in range(W+1)] for i in range(n+1)]

print(gold(weights,n,W))