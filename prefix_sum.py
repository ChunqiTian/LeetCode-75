# 1732. Find the Highest Altitude
class Solution(object):
    def largestAltitude(self, gain):
        alt = 0
        res = [0]
        for i in gain:
           alt += i
           res.append(alt) 
        return max(res)

# 724. Find Pivot Index
class Solution(object):
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]): return i
        return -1





