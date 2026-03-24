def fractional_knapsack(values, weights, W):
    n = len(values)
    
    # Create list of items with ratio
    items = []
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i]))
    
    # Sort items by ratio in descending order
    items.sort(reverse=True)
    
    total_value = 0.0
    
    for ratio, value, weight in items:
        if W >= weight:
            total_value += value
            W -= weight
        else:
            total_value += ratio * W
            break
    
    return total_value


# Example
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

print("Maximum value:", fractional_knapsack(values, weights, W))