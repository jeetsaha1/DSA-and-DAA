def knapsack_01(values, weights, W):
    n = len(values)
    
    # Create DP table (n+1) x (W+1)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Build table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],  # include
                    dp[i-1][w]                                # exclude
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][W]


# Example
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

print("Maximum value:", knapsack_01(values, weights, W))