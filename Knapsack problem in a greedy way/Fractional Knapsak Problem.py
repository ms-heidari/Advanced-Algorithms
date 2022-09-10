def fractional_knapsack(profit, weight, capacity):
    """Return maximum profit of items and their fractional amounts.

    (max_profit, fractions) is returned where max_profit is the maximum profit of
    items with total weight not more than capacity.
    fractions is a list where fractions[i] is the fraction that should be taken
    of item i, where 0 <= i < total number of items.

    profit[i] is the profit of item i and weight[i] is the weight of item i
    for 0 <= i < n where n is the number of items.

    capacity is the maximum weight.
    """
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(profit)))
    # contains ratios of profits to weight
    ratio = [p / w for p, w in zip(profit, weight)]
    # index is sorted according to profit-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_profit = 0
    fractions = [0] * len(profit)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_profit += profit[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity / weight[i]
            max_profit += profit[i] * capacity / weight[i]
            break

    return max_profit, fractions


n = int(input('Enter number of items: '))
profit = input('Enter the profits of the {} item(s) in order: '
               .format(n)).split()
profit = [int(v) for v in profit]
weight = input('Enter the positive weights of the {} item(s) in order: '
               .format(n)).split()
weight = [int(w) for w in weight]
capacity = int(input('Enter maximum weight: '))

max_profit, fractions = fractional_knapsack(profit, weight, capacity)
print('The maximum profit of items that can be carried:', max_profit)
print('The fractions in which the items should be taken:', fractions)