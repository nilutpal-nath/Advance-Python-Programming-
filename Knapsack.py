# 0/1 Knapsack Problem (Optimal Selection of Items)
# Experiment 6: Based on the bottom-up dynamic programming pseudocode

def knapsack_bottom_up(values, weights, W):
    n = len(values)
    # Create DP table with dimensions (n+1) x (W+1)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table dp[][] in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Main Program
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50

    max_profit = knapsack_bottom_up(values, weights, W)
    print(f"Items Values: {values}")
    print(f"Items Weights: {weights}")
    print(f"Knapsack Capacity: {W}")
    print(f"Maximum Profit: {max_profit}")  # Output: 220