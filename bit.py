
# 338. Counting Bits
def countBits(n):
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i & (i-1)] + 1
        return dp
    
# 136 . Single Number 
# pairs cancel out using ^
def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
    return res

# 1318. Minimum Flips to Make a OR b Equal to c
def minFlips(self, a, b, c):
    res = 0

    for i in range(32):
        abit = (a>>i) & 1 # to the last one and keep it, next to the last 2nd digit and keep it, then the 3rd...
        bbit = (a>>i) & 1
        cbit = (a>>i) & 1
        
        if cbit == 0: res += abit + bbit 
        else: # cbit == 1
            if abit == 0 and bbit == 0: res += 1
    return res



