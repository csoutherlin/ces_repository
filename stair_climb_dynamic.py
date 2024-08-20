def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Initialize an array to store the number of ways to reach each step
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    # Fill the array using the recurrence relation
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Test the function
print(climbStairs(3))  # Output: 3 (1+1+1, 1+2, 2+1)
print(climbStairs(4))  # Output: 5 (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)