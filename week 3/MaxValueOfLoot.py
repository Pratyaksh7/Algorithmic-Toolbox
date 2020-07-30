# using python3

def knapsack(W, weights, profits):
    ratios = [profits[i]/weights[i] for i in range(len(weights))]
    objects_included = [0] * len(weights)
    total_profit = 0
    while W > 0:

        for _ in range(len(weights)):
            maxRatioIndex = ratios.index(max(ratios))
            if weights[maxratioIndex] > W:
                W = 0
                objects_included[maxRatioIndex] = W/weights[maxRatioIndex]
            else:
                W = W - weights[maxRatioIndex]
                objects_included[maxRatioIndex] = 1
            ratios.remove(ratios[maxRatioIndex])
            weights.remove(weights[maxRatioIndex])

        for i in range(len(weights)):
            total_profit += (profits[i]*objects_included[i])

    return total_profit


n, W = map(int, input().split())
list1 = []
for i in range(n):
    val, weight = map(int, input().split())
    list1.append([val, weight])

profits = []
weights = []
list1 = dict(list1)
for i, j in list1.items():
    profits.append(i)
    weights.append(j)

opt_value = knapsack(W, weights, profits)
print("{:.4f}".format(opt_value))
