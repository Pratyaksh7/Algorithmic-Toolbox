# using python3

def knapsack(n, W, profits, weights):
    ratios = [profits[i] / weights[i] for i in range(n)]
    objects_included = [0] * n
    total_profit = 0
    ratios_index = [i for i in range(n)]

    for i in range(n):
        for j in range(i, 0, -1):
            if ratios[j] > ratios[j - 1]:
                ratios[j], ratios[j - 1] = ratios[j - 1], ratios[j]
                ratios_index[j], ratios_index[j -
                                              1] = ratios_index[j - 1], ratios_index[j]
            else:
                break

    for index in ratios_index:
        if W < weights[index]:
            objects_included[index] = W / weights[index]
            break
        else:
            W = W - weights[index]
            objects_included[index] = 1

    for i in range(n):
        total_profit += profits[i] * objects_included[i]

    return total_profit


n, W = map(int, input().split())
profits_weights = [list(map(int, input().split())) for i in range(n)]

print("%.4f" % knapsack(n, W, [profits_weights[i][0] for i in range(n)], [
      profits_weights[i][1] for i in range(n)]))
