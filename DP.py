# DP - 1D
# 1137. N-th Tribonacci Number
def tribonacci(self, n):
    if n == 0: return 0
    if n == 1 or n == 2: return 1

    dp = [0] * (n+1)
    dp[0], dp[1], dp[2] = 0, 1, 1

    for i in range(3, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    
    return dp[n]


# 746. Min Cost Climbing Stairs
def minCostClimbingStairs(self, cost):
    n = len(cost)
    dp = [0] * n

    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    return min(dp[n-1], dp[n-2])

# eg. dp = [1, 100, 2, 3, 3, 103]

# 198. House Robber
def rob(self, nums):
    n = len(nums)
    if n==1: return nums[0]
    dp = [0] * n

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2]) # skip or take
    return dp[-1]

#  790. Domino and Tromino Tiling
def numTilings(self, n):
    dp = [0] * (n+1)
    gap = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    # gap[0], gap[1] = 0,0 Already in the gap definition

    MOD = 10 ** 9 + 7

    for i in range(2, n+1):
        dp[i] = (dp[i-2] + dp[i-1] + 2 * gap[i-1]) % MOD
        gap[i] = (gap[i-1] + dp[i-2]) % MOD

    return dp[n]

# DP - Multidimensional - You no longer tracking "one state line", but a state space (grid or table)
    # Where each dimension represents an independent constraint. 
# 62. Unique Paths
# Method 1: DP - 2D
def uniquePaths(self, m, n):
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] # cur = top + left
    return dp[-1][-1]

# Method 2: Optimized DP - 1D
def uniquePaths(self, m, n):
    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j-1]
    return dp[-1]

# 1143. Longest Common Subsequence
def longestCommonSubsequence(self, text1, text2):
    n, m = len(text1), len(text2)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if text1[i] == text2[j]: dp[i][j] = dp[i-1][j-1] + 1
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]


# 714. Best Time to Buy and Sell Stock with Transaction Fee
def maxProfit(self, prices, fee):
    n = len(prices)
    hold, cash = [0] * n, [0] * n
    hold[0] = - prices[0]
    cash[0] = 0

    for i in range(1, n):
        hold[i] = max(hold[i-1], cash[i-1] - prices[i])
        cash[i] = max(cash[i-1], hold[i-1] + prices[i] - fee)
    return cash[-1]

# 72. Edit distance
def minDistance(self, word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        dp[i][0] = i

    for j in range(1, n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
            else: dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
    return dp[m][n] 










