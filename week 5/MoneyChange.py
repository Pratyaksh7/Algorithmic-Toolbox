# using python3
def minCoins(n, Coins):
    maxCoin = max(Coins)
    dic = {1: 1, 2: 2, 3: 1, 4: 1}
    if n > 4:
        if n % maxCoin == 0:
            print(n // 4)
        elif n % maxCoin == 1 or n % maxCoin == 2 or n % maxCoin == 3:
            print((n // 4) + 1)
    else:
        print(dic[n])


n = int(input())
Coins = [1, 3, 4]

minCoins(n, Coins)
